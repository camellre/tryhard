import pandas as pd
import numpy as np
from input_data import input_data

#def main_start():  
service_account_path = ''
spreadsheet_name = ''
worksheet_name = ''
item_report_files_paths = ["1", "2", "3"]
shipment_data_files_paths = []

while True:
    message = ("########## Dashboard ##########",
        "1.Data Files Paths Update",
        "Item Report file path:{}".format(*item_report_files_paths, sep = ","),
        "2.Google Service Account Key Update.",
        "3.Spreadsheet and Worksheet Name Update")
    
    print(*message, sep = '\n')
    command_selection = input("Please enter the command number:")



    
#filterer_data = input_data(item_report_files_paths, shipment_data_files_paths)
