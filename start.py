from inventory_management import stockupdate
from get_date import get_date

def main_start():

    a = stockupdate()
    while True:
        if a.initiation == "yes":
            with open("/home/rory/.tryhard_profile/scanned_tracking.txt", 'w') as output_file:
                for item in ["\n"]:
                    output_file.write(item + '\n')
            a.profile_update()
            a = stockupdate()
            a.input_data()
        else:
            break

    while True:
        a.dashboard_display()
        command_input = input("\n请输入选项数字，或者“q”键退出程序:")
        if command_input not in ["1", "2", "3", "db", 'q', "Q"]:
            print("\n已输入选项无效，请重新输入。")
            continue
        elif command_input in ['q', "Q"]:
            break
        elif command_input == '2':
            a.get_scanned()
            a.input_data()
            a.update_stock()
        elif command_input == '3':
            print(get_date())
        elif command_input == '1':
            a.profile_update()
            a = stockupdate()
            a.input_data()
        elif command_input == 'db':
            a.dashboard_display()

main_start()