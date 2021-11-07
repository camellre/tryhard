#Google service account key file path
service_account_path = '/home/rory/.tryhard_profile/profile.txt'

#AMAZON 2021 spreadsheet name
spreadsheet_amazon_2021_name = '' 

#AMAZON 2021 daily incoming stock worksheet name
amazon_2021_daily_name = '' 

#Amazon account order item report files paths. No duplicated records.
item_report_files_paths = '/home/rory/.tryhard_profile/item_report_path.txt'

#Amazon account order shipments report files paths. No duplicated records.
shipment_data_files_paths = '/home/rory/.tryhard_profile/shipment_report_path.txt'

#The scanned tracking numbers of daily incoming packages.
scanned_tracking_path = '' 

#Amazon account order records worksheet name.
amazon_2021_order_records_name = '' 

def service_account_key_output():
    try:
        service_account_key = ''
        with open(service_account_path, 'r') as f_1:
            service_account = f_1.readlines()
            for i in service_account:
                service_account_key.append(i[:-1])
    except:
        print("Service account path is not valid.")
        return None
    else:
        return service_account_key

def test(input = 0):
        switchers = {
        1: service_account_path,
        2: spreadsheet_amazon_2021_name,
        3: 
    }
    try:
        return switchers.get(int(selection_input))()
    except (TypeError, ValueError):
        print("Command selection is not valid.")
        return None
    