import pandas as pd
import numpy as np
from input_data import input_data
from input_worksheet import input_worksheet
from command_selection import command_selection

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

def dashboard_display():
    message = ("########## Dashboard ##########",
        "1.Data Files Paths Update",
        "Current Item Report file path:",
        "\n".join(item_report_files_paths),
        "\nCurrent shipment_data_files_paths:",
        "\n".join(shipment_data_files_paths),
        "\n2.Google Service Account Key Update.",
        "\n3.Spreadsheet and Worksheet Name Update")
    
    print(*message, sep = '\n')

dashboard_display()

while True:
    command_input = input("Please enter the command selection number:")
    if command_input == 'exit':
        break
    elif command_selection(command_input) == None:
        continue
    else:
        command_selection(command_input)



    
#filterer_data = input_data(item_report_files_paths, shipment_data_files_paths)
