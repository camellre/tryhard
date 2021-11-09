import pandas as pd
import numpy as np
from input_excel import input_excel
from input_csv import input_csv

def input_data(item_report_files_paths = [], shipment_data_files_paths = []):
    excel_output = input_excel(item_report_files_paths)
    csv_output = input_csv(shipment_data_files_paths)
    item_data = excel_output
    shipment_data = csv_output
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