import pandas as pd
import numpy as np
from find_tracking import find_tracking

def find_order(item_info, shipment_tracking_number,scanned_input = '', shipment_tracking_number_list = []):

    if scanned_input == '':
        print("Input is empty.")
        return None
    else:
        tracking_number_input = find_tracking(shipment_tracking_number_list, scanned_input)
        if tracking_number_input == None:
            return None
        elif tracking_number_input == 'Not Found!':
            return "Not Found!"
        else:
            try:
                confirmed_item_tracking_number = tracking_number_input
                searched_data_tracking = shipment_tracking_number.loc[
                    shipment_tracking_number['Carrier Name & Tracking Number'] == 
                        confirmed_item_tracking_number]

                searched_data_tracking.reset_index(inplace=True)
                print(searched_data_tracking)
                output_gsheet_list_combined = []

                for item in range(len(list(searched_data_tracking.loc[:,'Order ID']))):
                    for i in range(len(list(item_info.loc[:,'Order ID']))):
                        output_gsheet = []
                        output_gsheet_list = []
                        s_tracking_id = searched_data_tracking.loc[item, 'Order ID']
                        f_item_id = item_info.loc[i, 'Order ID']
                        s_item_subtotal = int(float(str(searched_data_tracking.loc[item, 'Subtotal'][1:]).replace(",", ''))*1000)
                        f_item_price = int(float(str(item_info.loc[i, 'Purchase Price Per Unit']).replace(",", ""))*1000)

                        if s_tracking_id == f_item_id and s_item_subtotal % f_item_price == 0:
                            searched_data_list = item_info.loc[i, ['Order Date', 'Order ID', 'Title', 
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
            except:
                print("Item or shipments data are not valid.")
                return None
            else:
                return output_gsheet_list_combined