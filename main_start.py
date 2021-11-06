import pandas as pd
import numpy as np
from input_data import input_data

#def main_start():  
service_account_path = ''
spreadsheet_name = ''
worksheet_name = ''
item_report_files_paths = ["1", "2", "3"]
shipment_data_files_paths = ["1", "2", "3"]
scanned_tracking_path = ''

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
    command_selection = input("Please enter the command number:")



    
#filterer_data = input_data(item_report_files_paths, shipment_data_files_paths)
