import pandas as pd
import numpy as np
from input_data import input_data
from input_worksheet import input_worksheet
from stock_update import stock_update

#def main_start():  
#Google service account key file path
service_account_path = '' 

#AMAZON 2021 spreadsheet name
spreadsheet_amazon_2021_name = '' 

#AMAZON 2021 daily incoming stock worksheet name
amazon_2021_daily_name = '' 

#Amazon account order item report files paths. No duplicated records.
item_report_files_paths = ["1", "2", "3"] 

#Amazon account order shipments report files paths. No duplicated records.
shipment_data_files_paths = ["1"] 

#The scanned tracking numbers of daily incoming packages.
scanned_tracking_path = '' 

#Amazon account order records worksheet name.
amazon_2021_order_records_name = '' 

#The filtered data extracted from the items report and shipments report with correct columns.
filtered_data = input_data(item_report_files_paths, shipment_data_files_paths)

#The daily incoming stock worksheet access(the worksheet input as a class) initiation.
work_sheet_daily = input_worksheet(service_account_path, spreadsheet_amazon_2021_name, 
    amazon_2021_daily_name)

while True:
    message = ("########## Dashboard ##########",
        "1.Data Files Paths Update",
        "Current Item Report file path:",
        "\n".join(item_report_files_paths),
        "Current shipment_data_files_paths:",
        "\n".join(shipment_data_files_paths),
        "2.Google Service Account Key Update.",
        "3.Spreadsheet and Worksheet Name Update")
    
    print(*message, sep = '\n')
    command_selection_input = input("Please enter the command number:")
    



    
#filterer_data = input_data(item_report_files_paths, shipment_data_files_paths)
