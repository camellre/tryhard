import pygsheets

def input_worksheet(service_account_path = '', spreadsheet_name = '', worksheet_name = ''):
    if service_account_path == '':
        print("Google service account key is empty.")
        return None
    elif spreadsheet_name == '':
        print("Spreadsheet name is empty.")
        return None
    elif worksheet_name == '':
        print("Worksheet name is empty.")
        return None
    else:
        try:
            gc = pygsheets.authorize(service_file=service_account_path)
            spread_sheet = gc.open(spreadsheet_name)
            work_sheet = spread_sheet.worksheet_by_title(worksheet_name)
        except:
            print("The spreadsheet can not import, please check the service account key, spreadsheet_name, or worksheet_name.")
            return None
        else:
            return work_sheet