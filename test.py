import pandas as pd
import numpy as np
import openpyxl
import pygsheets

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
            self.scanned_file = stockupdate.paths[3]
            self.spreadsheet_name = stockupdate.read_paths(stockupdate.paths[0])[1]
            self.worksheet_name = stockupdate.read_paths(stockupdate.paths[0])[2]
        except:
            print("The file paths are empty, please enter file paths.")
            self.g_service_key = ''
            self.item_file = []
            self.shipment_file = []
            self.scanned_file = stockupdate.paths[3]
            self.spreadsheet_name = ''
            self.worksheet_name = ''

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
        selection = input("Please enter selection:")
        if selection not in ["1", "2", "3", "4", "5"]:
            print("Selection is not valid.")
            return None
        elif selection == '1':
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

a = stockupdate()