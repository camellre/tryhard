import gspread
from get_date import get_date

Paths = (
    "/Users/rory/Downloads/service_account.json",
    "/Users/rory/tryhard/profile.txt",
    "/Users/rory/tryhard/scanned_list.txt",
    )

gc = gspread.service_account(filename=Paths[0])

spreadsheet_1 = gc.open("test-database")

worksheet_1 = spreadsheet_1.worksheet("database-1")

prompt_tuple = (
    "\n请扫描或输入快递单号（手动输入需要完整单号，按“Q”键退出）:", 
    "\n请输入或扫描产品UPC码（无法输入UPC请按回车跳过）:", 
    "\n请输入产品数量:", 
    "\n请输入该产品备注:",
    )

def read_paths(file_path):
        path_output = []
        with open(file_path, 'r') as f:
            file_content = f.readlines()
            for i in file_content:
                path_output.append(i[:-1])
        return path_output
    
def file_update(input, file_path):
    with open(file_path, 'w') as output_file:
        for item in input:
            output_file.write(item + '\n')

def muti_items_confirmation():
    while True:
        input_0 = input("\n该快递单号已扫描，是否需要录入同一快递单号下的其他货品？（Y / N）:")
        if input_0 not in ("Y", "y", "N", "n"):
            print("\n输入无效，请重新输入。")
            continue
        elif input_0 in ("Y", "y"):
            return "yes"
        elif input_0 in ("N", "n"):
            return "no"

def row_input(row_data, a, scanned_list):
    if a == len(prompt_tuple):
        while True:
            print("")
            print(*row_data, sep="\n")
            data_confirmation = input("请核查录入信息是否正确，并确认是否录入该货品记录？( Y / N ):")
            if data_confirmation not in ("Y", "y", "N", "n"):
                print("输入无效，请重新输入!")
                continue
            elif data_confirmation in ("Y", "y"):
                row_data.append("y")
                return row_data
            elif data_confirmation in ("N", "n"):
                row_data.pop()
                return row_data
    else:
        for i in range(a, len(prompt_tuple)):
            data_input = input(prompt_tuple[i])
            if data_input in ("b", "B") and row_data == []:
                return row_data
            elif data_input in ("b", "B"):
                row_data.pop()
                return row_data
            elif data_input in ("q", "Q"):
                row_data.append("exit")
                return row_data
            elif data_input == "" and row_data == []:
                print("\n快递单号不能为空，请重新输入!")
                return row_data
            elif data_input in scanned_list and row_data == []:
                scanned_confirmation = muti_items_confirmation()
                if scanned_confirmation == "yes":
                    row_data.append(data_input)
                    return row_data
                else:
                    return row_data
            else:
                row_data.append(data_input)
                return row_data

def data_input(prompt_tuple, worksheet, row_number, scanned_list):
    try:
        while True:
            row_data = []
            while len(row_data) <= len(prompt_tuple):
                if "exit" in row_data:
                    return "exit"
                else:
                    row_data = row_input(row_data, len(row_data), scanned_list)
            else:
                row_data.pop()
                today_date = get_date()
                row_data.insert(0, today_date)
                worksheet.update("A{}:F{}".format(row_number, row_number), [row_data])
                row_number += 1
                scanned_list.append(row_data[1])
                file_update([str(row_number)], Paths[1])
                file_update(scanned_list, Paths[2])
    except:
        print("内部错误! 请重新进入入库系统，并录入该货品信息.")
        pass

def initiation_app():
    try:
        scanned_list = read_paths(Paths[2])
        row = int(read_paths(Paths[1])[0])
    except:
        print("\n已扫描快递单号，或起始表格行，数据导入异常，请检查后重新启动程序。")
        pass
    else:
        data_input(prompt_tuple, worksheet_1, row, scanned_list)

def update_stock():
    mgs = ("############################################ 每日入库 ############################################",
            "\n                                       1.扫描Tracking入库",
            "                                       2.更新起始表格行号码")
    
    while True:
        print(*mgs, sep = '\n')
        selection = input("\n请输入选项号码:")
        if selection in ("q", "Q"):
            break
        elif selection not in ("1", "2"):
            print("\n已输入的选项有误，请重新输入。")
            continue
        elif selection == "1":
            initiation_app()
        elif selection == "2":
            row_update = input("\n请输入新的起始表格行号码:")
            file_update([str(row_update)], Paths[1])

update_stock()