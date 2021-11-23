import pandas as pd
import numpy as np
import pygsheets
import os
from get_date import get_date

class management_tools():
    @staticmethod
    def read_paths(file_path):
        path_output = []
        with open(file_path, 'r') as f:
            file_content = f.readlines()
            for i in file_content:
                path_output.append(i[:-1])
        return path_output
    
    @staticmethod
    def file_update(input, file_path):
        with open(file_path, 'w') as output_file:
            for item in input:
                output_file.write(item + '\n')

    @staticmethod
    def input_worksheet(service_account_path = '', spreadsheet_name = '', worksheet_name = ''):
        gc = pygsheets.authorize(service_file=service_account_path)
        spread_sheet = gc.open(spreadsheet_name)
        work_sheet = spread_sheet.worksheet_by_title(worksheet_name)
        return work_sheet

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

    @staticmethod
    def outbound_confirmed():
        while True:
            input = ("\n请确认产品是否可以直接发货（封条是否完好，产品是否为新的）（ y / n）？")
            if input not in ("Y", "y", "N", "n"):
                print("\n输入无效，请重新输入。")
                continue
            elif input in ("Y", "y"):
                return "yes"
            elif input in ("N", "n"):
                return "no"

class stockupdate():
    paths = (
        '/home/rory/.tryhard_profile/profile.txt',
        '/home/rory/.tryhard_profile/scanned_tracking.txt'
    )
    def __init__(self):

        try:
            self.g_service_key = management_tools.read_paths(stockupdate.paths[0])[0]
            self.order_database_name = management_tools.read_paths(stockupdate.paths[0])[1]
            self.order_item_sheetname = management_tools.read_paths(stockupdate.paths[0])[2]
            self.order_shipments_sheetname = management_tools.read_paths(stockupdate.paths[0])[3]
            self.stock_spreadsheet_name = management_tools.read_paths(stockupdate.paths[0])[4]
            self.stock_worksheet_name = management_tools.read_paths(stockupdate.paths[0])[5]
            self.stock_update_row = management_tools.read_paths(stockupdate.paths[0])[6]
            self.scanned_tracking = []
            self.stock_update_sheet = ""
            self.item_filtered = pd.DataFrame()
            self.shipment_tracking = pd.DataFrame()
            self.shipment_tracking_list = []
            self.initiation = 'no'
        except:
            print("未检测到Google账户及表格名称，请按照如下步骤更新：")
            self.g_service_key = ""
            self.order_database_name = ""
            self.order_item_sheetname = ""
            self.order_shipments_sheetname = ""
            self.stock_spreadsheet_name = ""
            self.stock_worksheet_name = ""
            self.initiation = 'yes'
    
    def get_scanned(self):

        try:
            with open(stockupdate.paths[1], 'r') as f:
                scanned_tracking_number_list = f.readlines()
                for i in scanned_tracking_number_list:
                    self.scanned_tracking.append(i[:-1])
        except:
            print("已扫描Tracking号数据异常，无法导入。")
            pass

    def dashboard_display(self):

        message = ("############################################# 主菜单 #############################################",
            "\n                                         1.Google账户及表格名称设置",
            "                                         2.每日入库",
            "                                         3.显示今天日期",
            "                                         4.查询订单")
        
        print(*message, sep = '\n')

    def input_data(self):

        try:
            self.stock_update_sheet = management_tools.input_worksheet(self.g_service_key,
                self.stock_spreadsheet_name, self.stock_worksheet_name)
            order_items = management_tools.input_worksheet(self.g_service_key, self.order_database_name,
                self.order_item_sheetname).get_as_df(empty_value = "")
            order_shipments = management_tools.input_worksheet(self.g_service_key, self.order_database_name, 
                self.order_shipments_sheetname).get_as_df(empty_value = "")
            self.item_filtered = order_items.loc[:,['Order Date', 'Order ID', 'Title', 'ASIN/ISBN', 
                'Condition', 'Seller','List Price Per Unit', 'Purchase Price Per Unit', 'Quantity']]
            self.shipment_tracking = order_shipments.loc[:,['Order ID','Subtotal','Carrier Name & Tracking Number']]
            self.shipment_tracking_list = self.shipment_tracking['Carrier Name & Tracking Number'].tolist()
        except:
            print("导入数据异常，请检查Google账户及表格名称设置。")
            pass

    def profile_update(self):

        mg = ("####################################### Google账户及表格名称设置 #######################################",
            '\n                                1.Google账户密钥路径（File Path）',
            "                                2.Amazon数据库Google Sheet名称（SpreadSheet Name）",
            "                                3.基于item的数据WorkSheet名称（item report）",
            "                                4.基于shipment的数据Worksheet名称（shipment and order report）",
            "                                5.入库表格Google Sheet名称（SpreadSheet Name）",
            "                                6.入库表格Work Sheet名称（WorkSheet Name）",
            "                                7.更新起始表格行号码（Beginning Row Number）")
        print(*mg, sep = '\n')
        while True:
            selection = input("\n请输入选项号码:")
            if selection in ["q", "Q"]:
                break
            elif selection not in ["1", "2", "3", "4", "5", "6", "7"]:
                print("\n已输入的选项有误，请重新输入。")
                continue
            else:
                if selection == '1':
                    self.g_service_key = input("\n请输入 Google账户密钥路径:")
                    output_temp_1 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp_1, stockupdate.paths[0])
                elif selection == '2':
                    self.order_database_name = input("\n请输入 Amazon数据库Google Sheet名称:")
                    output_temp_2 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp_2, stockupdate.paths[0])
                elif selection == '3':
                    self.order_item_sheetname = input("\n请输入 基于item的数据WorkSheet名称:")
                    output_temp_3 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp_3, stockupdate.paths[0])
                elif selection == '4':
                    self.order_shipments_sheetname = input("\n请输入 基于shipment的数据Worksheet名称:")
                    output_temp_4 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp_4, stockupdate.paths[0])
                elif selection == '5':
                    self.stock_spreadsheet_name = input("\n请输入 入库表格Google Sheet名称:")
                    output_temp_5 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp_5, stockupdate.paths[0])
                elif selection == '6':
                    self.stock_worksheet_name = input("\n请输入 入库表格Work Sheet名称:")
                    output_temp_6 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp_6, stockupdate.paths[0])
                elif selection == '7':
                    self.stock_update_row = input("\n请输入 更新起始表格行号码:")
                    output_temp_7 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp_7, stockupdate.paths[0])

    def find_tracking(self, scanned_input):

        tracking_output = "Not Found!"
        scanned_input = scanned_input.upper()
        for i in range(len(self.shipment_tracking_list)):
            if scanned_input in self.shipment_tracking_list[i]:
                tracking_output = self.shipment_tracking_list[i]
        return tracking_output

    def find_order(self, scanned_input):

        confirmed_tracking = self.find_tracking(scanned_input)
        if confirmed_tracking == "Not Found!":
            return "Not Found!"
        else:
            searched_data_tracking = self.shipment_tracking.loc[
                self.shipment_tracking['Carrier Name & Tracking Number'] == confirmed_tracking
            ]

            searched_data_tracking.reset_index(inplace=True)
            output_gsheet_list_combined = []

            for item in range(len(list(searched_data_tracking.loc[:,'Order ID']))):
                for i in range(len(list(self.item_filtered.loc[:,'Order ID']))):
                    output_gsheet = []
                    output_gsheet_list = []
                    s_tracking_id = searched_data_tracking.loc[item, 'Order ID']
                    f_item_id = self.item_filtered.loc[i, 'Order ID']
                    s_item_subtotal = int(float(str(searched_data_tracking.loc[item, 'Subtotal'][1:]).replace(",", ''))*1000)
                    f_item_price = int(float(str(self.item_filtered.loc[i, 'Purchase Price Per Unit']).replace(",", ""))*1000)

                    if s_tracking_id == f_item_id and s_item_subtotal % f_item_price == 0:
                        searched_data_list = self.item_filtered.loc[i, ['Order Date', 'Order ID', 'Title', 
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
            return output_gsheet_list_combined

    def update_stock(self):

        mgs = ("############################################ 每日入库 ############################################",
                "\n                                       1.扫描Tracking入库",
                "                                       2.更新起始表格行号码")
        print(*mgs, sep = '\n')

        while True:
            selection = input("\n请输入选项号码:")
            if selection in ["q", "Q"]:
                break
            elif selection not in ["1", "2"]:
                print("\n已输入的选项有误，请重新输入。")
                continue
            else:
                if selection == "2":
                    self.stock_update_row = input("\n请输入 更新起始表格行号码:")
                    output_temp = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
                        self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
                        self.stock_update_row]
                    management_tools.file_update(output_temp, stockupdate.paths[0])
                elif selection == "1":
                    self.database_update()

    def database_update(self):
        
        while True:
            row = int(self.stock_update_row)
            a = input('\n请扫描或输入快递单号（手动输入至少8位以上）:')
            a = a.upper()

            if a == 'Q':
                break
            elif a == '':
                print('\n输入不能为空，请重新输入。')
                continue
            elif a != '' and a != 'Q':
                b = self.find_order(a)
                if b == "Not Found!":
                    if a in self.scanned_tracking:
                        print('\n该快递单号已录入，请扫描或输入下一个。')
                        continue
                    else:
                        print("\n未查询到快递单号记录！需要手动录入产品信息。")
                        stockupdate.play_sound(exceptions = 'not_found')
                        item_title = input("\n请输入或扫描产品UPC码，或者输入产品品牌和型号:")
                        if item_title in ["b", "B"]:
                            continue
                        else:
                            item_quantity = input("\n请输入产品数量:")
                            if item_quantity in ["b", "B"]:
                                continue
                            else:
                                self.scanned_tracking.append(a)
                                self.stock_update_sheet.update_value('D{}'.format(row), item_title)
                                self.stock_update_sheet.update_value('J{}'.format(row), item_quantity)
                                self.stock_update_sheet.update_value('A{}'.format(row), get_date())
                                self.stock_update_sheet.update_value('L{}'.format(row), a)

                                item_status = management_tools.outbound_confirmed()
                                if item_status == "yes":
                                    cell_0 = self.stock_update_sheet.cell("D{}".format(row))
                                    cell_0.color = (0.4,1,0.4,0.4)
                                    row += 1
                                    self.stock_update_row = str(row)
                                    continue
                                else:
                                    row += 1
                                    self.stock_update_row = str(row)
                                    continue
                    
                elif b == []:
                    if a in self.scanned_tracking:
                        print('Already scanned.')
                        continue
                    else:
                        print("\n未查询到快递单号记录！需要手动录入产品信息。")
                        stockupdate.play_sound(exceptions = 'not_found')
                        item_title = input("\n请输入或扫描产品UPC码，或者输入产品品牌和型号:")
                        if item_title in ["b", "B"]:
                            continue
                        else:
                            item_quantity = input("\n请输入产品数量:")
                            if item_quantity in ["b", "B"]:
                                continue
                            else:
                                self.scanned_tracking.append(a)
                                self.stock_update_sheet.update_value('D{}'.format(row), item_title)
                                self.stock_update_sheet.update_value('J{}'.format(row), item_quantity)
                                self.stock_update_sheet.update_value('A{}'.format(row), get_date())
                                self.stock_update_sheet.update_value('L{}'.format(row), a)
                                
                                item_status = management_tools.outbound_confirmed()
                                if item_status == "yes":
                                    cell_0 = self.stock_update_sheet.cell("D{}".format(row))
                                    cell_0.color = (0.4,1,0.4,0.4)
                                    row += 1
                                    self.stock_update_row = str(row)
                                    continue
                                else:
                                    row += 1
                                    self.stock_update_row = str(row)
                                    continue

                else:
                    if a in self.scanned_tracking:
                        print('\n该快递单号已录入，请扫描或输入下一个。')
                        continue
                    else:
                        self.scanned_tracking.append(a)
                        print(*b)
                        for i in range(len(b)):
                            stockupdate.play_sound(numbers = str(b[i][8]), conditions = str(b[i][4]))
                            self.stock_update_sheet.update_value('A{}'.format(row), get_date())
                            self.stock_update_sheet.update_row(row, b[i], col_offset=1)
                            
                            item_status = management_tools.outbound_confirmed()
                            if item_status == "yes":
                                cell_0 = self.stock_update_sheet.cell("D{}".format(row))
                                cell_0.color = (0.4,1,0.4,0.4)
                                row += 1
                                self.stock_update_row = str(row)
                                continue
                            else:
                                row += 1
                                self.stock_update_row = str(row)
                                continue

        with open(stockupdate.paths[1], 'w') as output_file:
            for item in self.scanned_tracking:
                output_file.write(item + '\n')
        
        output_temp_1 = [self.g_service_key, self.order_database_name, self.order_item_sheetname, 
            self.order_shipments_sheetname, self.stock_spreadsheet_name, self.stock_worksheet_name, 
            self.stock_update_row]
        management_tools.file_update(output_temp_1, stockupdate.paths[0])
