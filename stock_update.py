import pandas as pd
import numpy as np
import openpyxl
import pygsheets
import os
from get_date import get_date

class stockupdate():
    paths = (
        '/home/rory/.tryhard_profile/profile.txt',
        '/home/rory/.tryhard_profile/item_report_path.txt',
        '/home/rory/.tryhard_profile/shipment_report_path.txt',
        '/home/rory/.tryhard_profile/scanned_tracking.txt'
        )
    def __init__(self):
        try:
            self.g_service_key = stockupdate.read_paths(stockupdate.paths[0])[0]
            self.item_file = stockupdate.read_paths(stockupdate.paths[1])
            self.shipment_file = stockupdate.read_paths(stockupdate.paths[2])
            self.scanned_tracking = stockupdate.get_scanned(stockupdate.paths[3])
            self.spreadsheet_name = stockupdate.read_paths(stockupdate.paths[0])[1]
            self.worksheet_name = stockupdate.read_paths(stockupdate.paths[0])[2]
            self.worksheet_content = stockupdate.input_worksheet(self.g_service_key, self.spreadsheet_name, self.worksheet_name)
            self.item_data_filtered = stockupdate.input_data(self.item_file, self.shipment_file)[0]
            self.shipment_tracking = stockupdate.input_data(self.item_file, self.shipment_file)[1]
            self.shipment_tracking_list = stockupdate.input_data(self.item_file, self.shipment_file)[2]
            self.initiation = 'no'
        except:
            print("One of the file paths are empty or not valid, please check file paths and contents.")
            self.g_service_key = ''
            self.item_file = []
            self.shipment_file = []
            self.scanned_tracking = []
            self.spreadsheet_name = ''
            self.worksheet_name = ''
            self.worksheet_content = ''
            self.item_data_filtered = ''
            self.shipment_tracking = ''
            self.shipment_tracking_list = ''
            self.initiation = 'yes'

    @staticmethod
    def read_paths(file_path):
        try:
            path_output = []
            with open(file_path, 'r') as f:
                file_content = f.readlines()
                for i in file_content:
                    path_output.append(i[:-1])
        except:
            print("File path is not valid.")
            return None
        else:
            return path_output
    
    @staticmethod
    def file_update(input, file_path):
        with open(file_path, 'w') as output_file:
            for item in input:
                output_file.write(item + '\n')
    
    def paths_update(self):
        while True:
            initiation_input_message = ('1.Google Service Account key path',
                "\n2.Spreadsheet name",
                "\n3.Worksheet name",
                "\n4.item report file paths",
                "\n5.shipment report file paths")
            print(*initiation_input_message)
            selection = input("Please enter the command selection number:")
            if selection == "exit":
                break
            elif selection not in ["1", "2", "3", "4", "5"]:
                print("Selection is not valid.")
                continue
            else:
                if selection == '1':
                    self.g_service_key = input("Please enter new google service account key:")
                    output_temp_1 = [self.g_service_key, self.spreadsheet_name, self.worksheet_name]
                    stockupdate.file_update(output_temp_1, stockupdate.paths[0])
                elif selection == '2':
                    self.spreadsheet_name = input("Please enter new spreadsheet name:")
                    output_temp_2 = [self.g_service_key, self.spreadsheet_name, self.worksheet_name]
                    stockupdate.file_update(output_temp_2, stockupdate.paths[0])
                elif selection == '3':
                    self.worksheet_name = input("Please enter new worksheet name:")
                    output_temp_3 = [self.g_service_key, self.spreadsheet_name, self.worksheet_name]
                    stockupdate.file_update(output_temp_3, stockupdate.paths[0])
                elif selection == '4':
                    item_file_temp = []
                    while True:
                        item_file_input = input ("Please enter new item report file paths:")
                        if item_file_input == "exit" and item_file_temp == []:
                            break
                        elif item_file_input == "exit" and item_file_temp != []:
                            self.item_file = item_file_temp
                            stockupdate.file_update(self.item_file, stockupdate.paths[1])
                            break
                        else:
                            item_file_temp.append(item_file_input)
                elif selection == '5':
                    shipment_file_temp = []
                    while True:
                        shipment_file_input = input ("Please enter new shipment report file paths:")
                        if shipment_file_input == "exit" and shipment_file_temp == []:
                            break
                        elif shipment_file_input == "exit" and shipment_file_temp != []:
                            self.shipment_file = shipment_file_temp
                            stockupdate.file_update(self.shipment_file, stockupdate.paths[2])
                            break
                        else:
                            shipment_file_temp.append(shipment_file_input)

    @staticmethod
    def input_worksheet(service_account_path = '', spreadsheet_name = '', worksheet_name = ''):
        try:
            gc = pygsheets.authorize(service_file=service_account_path)
            spread_sheet = gc.open(spreadsheet_name)
            work_sheet = spread_sheet.worksheet_by_title(worksheet_name)
        except:
            print("The spreadsheet can not import, please check the service account key, spreadsheet_name, or worksheet_name.")
            return None
        else:
            return work_sheet

    @staticmethod
    def input_excel(excel_path):
        try:
            files_list = []
            for filename in excel_path:
                files_list.append(pd.read_excel(filename))
            file_data = pd.concat(files_list, ignore_index=True).fillna("")
        except:
            print('The excel file path is not valid, please check the file path.')
            return None
        else:
            return file_data
    
    @staticmethod
    def input_csv(csv_path):
        try:
            files_list = []
            for filename in csv_path:
                files_list.append(pd.read_csv(filename))
            file_data = pd.concat(files_list, ignore_index=True).fillna("")
        except:
            print('The csv file path is not valid, please check the file path.')
            return None
        else:
            return file_data

    @staticmethod
    def input_data(item_report_files_paths, shipment_data_files_paths):
        item_data = stockupdate.input_excel(item_report_files_paths)
        shipment_data = stockupdate.input_csv(shipment_data_files_paths)
        try:
            item_data_filtered = item_data.loc[:,['Order Date', 'Order ID', 'Title', 'ASIN/ISBN', 'Condition', 'Seller','List Price Per Unit', 'Purchase Price Per Unit', 'Quantity']].fillna("")
            shipment_tracking = shipment_data.loc[:,['Order ID','Subtotal','Carrier Name & Tracking Number']].fillna("")
            shipment_tracking_list = shipment_tracking['Carrier Name & Tracking Number'].tolist()
        except:
            print("Imported data are not valid, please check the excel or csv files.")
            return None
        else:
            filtered_data = [item_data_filtered, shipment_tracking, shipment_tracking_list]
            return filtered_data

    @staticmethod
    def play_sound(numbers = '0', conditions = 'new', exceptions = 'none'):
        if exceptions == 'not_found':
            file_exceptions = '/home/rory/tryhard-main/audio-numbers/{}.mp3'.format(exceptions)
            os.system('mpg123 -q ' + file_exceptions)
        else:
            if conditions == 'new':
                file_numbers = '/home/rory/tryhard-main/audio-numbers/{}.mp3 '.format(numbers)
                file_conditions = '/home/rory/tryhard-main/audio-numbers/{}.mp3'.format(conditions)
                os.system('mpg123 -q ' + file_numbers + file_conditions)
            else:
                file_numbers = '/home/rory/tryhard-main/audio-numbers/{}.mp3 '.format(numbers)
                file_conditions = '/home/rory/tryhard-main/audio-numbers/{}.mp3'.format('used')
                os.system('mpg123 -q ' + file_numbers + file_conditions)

    def dashboard_display(self):
        message = ("########## Dashboard ##########",
            "Current Item Report file path:",
            "\n".join(self.item_file),
            "Current shipment_data_files_paths:",
            "\n".join(self.shipment_file),
            "Current Google Service Account Key:",
            self.g_service_key,
            "Current Spreadsheet and Worksheet Name:",
            self.spreadsheet_name,
            self.worksheet_name,
            "1.Data Files Paths, Google Service Account Key, and Spreadsheet and Worksheet Name Update",
            "2.Daily Incoming Stock Update.",
            "3.Show the date of today.")
        
        print(*message, sep = '\n')

    @staticmethod
    def get_scanned(scanned_tracking_path):
        scanned_tracking_filtered = []
        try:
            with open(scanned_tracking_path, 'r') as scanned_tracking_number:
                scanned_tracking_number_list = scanned_tracking_number.readlines()
                for i in scanned_tracking_number_list:
                    scanned_tracking_filtered.append(i[:-1])
        except:
            print("Scanned tracking number data is not valid.")
            return None
        else:
            return scanned_tracking_filtered

    def find_tracking(self, scanned_input):
        try:
            tracking_output = 'Not Found!'
            scanned_input = scanned_input.upper()
            for i in range(len(self.shipment_tracking_list)):
                if scanned_input in self.shipment_tracking_list[i]:
                    tracking_output = self.shipment_tracking_list[i]
        except:
            print("The tracking number data or input is not valid.")
            return None
        else:
            return tracking_output


    def find_order(self, scanned_input):

        tracking_number_input = self.find_tracking(scanned_input)
        if tracking_number_input == None:
            return None
        elif tracking_number_input == 'Not Found!':
            return "Not Found!"
        else:
            try:
                confirmed_item_tracking_number = tracking_number_input
                searched_data_tracking = self.shipment_tracking.loc[
                    self.shipment_tracking['Carrier Name & Tracking Number'] == 
                        confirmed_item_tracking_number]

                searched_data_tracking.reset_index(inplace=True)
                print(searched_data_tracking)
                output_gsheet_list_combined = []

                for item in range(len(list(searched_data_tracking.loc[:,'Order ID']))):
                    for i in range(len(list(self.item_data_filtered.loc[:,'Order ID']))):
                        output_gsheet = []
                        output_gsheet_list = []
                        s_tracking_id = searched_data_tracking.loc[item, 'Order ID']
                        f_item_id = self.item_data_filtered.loc[i, 'Order ID']
                        s_item_subtotal = int(float(str(searched_data_tracking.loc[item, 'Subtotal'][1:]).replace(",", ''))*1000)
                        f_item_price = int(float(str(self.item_data_filtered.loc[i, 'Purchase Price Per Unit']).replace(",", ""))*1000)

                        if s_tracking_id == f_item_id and s_item_subtotal % f_item_price == 0:
                            searched_data_list = self.item_data_filtered.loc[i, ['Order Date', 'Order ID', 'Title', 
                                'ASIN/ISBN', 'Condition', 'Seller', 'List Price Per Unit', 'Purchase Price Per Unit']]
                            searched_data_list = searched_data_list.tolist()
                            searched_data_list.append(str(int(s_item_subtotal / f_item_price)))
                            searched_data_list.append(str(searched_data_tracking.loc[item, 'Carrier Name & Tracking Number']))
                            searched_data_list.append(scanned_input)
                            output_gsheet.append(searched_data_list)
                            
                            for i in range(len(output_gsheet)):
                                output_gsheet_list = output_gsheet[i]
                                output_gsheet_list = list(map(str, output_gsheet_list))
                            output_gsheet_list_combined.append(output_gsheet_list)
                            break
            except:
                print("Item or shipments data are not valid.")
                return None
            else:
                return output_gsheet_list_combined

    def update_stock(self):
        while True:
            row_0 = input('Please enter the beginning row number where it should start:')
            if row_0 == '':
                print('The beginning row must be entered.')
                continue
            elif row_0 == 'exit':
                return None
            else:
                row = int(row_0)
                break

        while True:
            
            a = input('Please scan tracking number:')
            a = a.upper()
            if a == 'EXIT':
                break
            elif a == '':
                print('The tracking number must be scanned.')
                continue
            elif a != '' and a != 'EXIT':
                b = self.find_order(a)
                if b == "Not Found!":
                    if a in self.scanned_tracking:
                        print('Already scanned.')
                        continue
                    else:
                        print("Not Found!")
                        stockupdate.play_sound(exceptions = 'not_found')
                        item_title = input("Please enter the item name or UPC code:")
                        if item_title in ["b", "B"]:
                            continue
                        else:
                            item_quantity = input("Please enter the item quantity:")
                            if item_quantity in ["b", "B"]:
                                continue
                            else:
                                self.scanned_tracking.append(a)
                                self.worksheet_content.update_value('D{}'.format(row), item_title)
                                self.worksheet_content.update_value('J{}'.format(row), item_quantity)
                                self.worksheet_content.update_value('A{}'.format(row), get_date())
                                self.worksheet_content.update_value('L{}'.format(row), a)
                                row += 1
                                continue
                    
                elif b == []:
                    if a in self.scanned_tracking:
                        print('Already scanned.')
                        continue
                    else:
                        print("Tracking number is not valid or order is too old.")
                        stockupdate.play_sound(exceptions = 'not_found')
                        item_title = input("Please enter the item name or UPC code:")
                        if item_title in ["b", "B"]:
                            continue
                        else:
                            item_quantity = input("Please enter the item quantity:")
                            if item_quantity in ["b", "B"]:
                                continue
                            else:
                                self.scanned_tracking.append(a)
                                self.worksheet_content.update_value('D{}'.format(row), item_title)
                                self.worksheet_content.update_value('J{}'.format(row), item_quantity)
                                self.worksheet_content.update_value('A{}'.format(row), get_date())
                                self.worksheet_content.update_value('L{}'.format(row), a)
                                row += 1
                                continue

                else:
                    if a in self.scanned_tracking:
                        print('Already scanned.')
                        continue
                    else:
                        self.scanned_tracking.append(a)
                        print(*b)
                        for i in range(len(b)):
                            stockupdate.play_sound(numbers = str(b[i][8]), conditions = str(b[i][4]))
                            self.worksheet_content.update_value('A{}'.format(row), get_date())
                            self.worksheet_content.update_row(row, b[i], col_offset=1)
                            row += 1

        with open(stockupdate.paths[3], 'w') as output_file:
            for item in self.scanned_tracking:
                output_file.write(item + '\n')