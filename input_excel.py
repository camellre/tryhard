import pandas as pd

def input_excel(excel_path = []):
    if excel_path == []:
        print('The csv file path is empty, please check the file path.')
        return None
    else:
        try:
            files_list = []
            for filename in excel_path:
                files_list.append(pd.read_excel(filename))
            file_data = pd.concat(files_list, ignore_index=True).fillna("")
        except:
            print('The excel file path is not valid, please check the file path.')
            return None
        else:
            return file_data