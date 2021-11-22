from stock_update import stockupdate
from get_date import get_date

def main_start():

    a = stockupdate()
    while True:
        if a.initiation == "yes":
            print("Data files are empty, initiation is needed.")
            with open("/home/rory/.tryhard_profile/scanned_tracking.txt", 'w') as output_file:
                for item in ["\n"]:
                    output_file.write(item + '\n')
            a.paths_update()
            a = stockupdate()
        else:
            break

    a.dashboard_display()

    while True:
        command_input = input("Please enter the command selection number:")
        if command_input not in ["1", "2", "3", "4", "db", 'exit', "EXIT"]:
            print("Invalid input, please enter again.")
            continue
        elif command_input in ['exit', "EXIT"]:
            break
        elif command_input == '2':
            a.update_stock()
        elif command_input == '3':
            print(get_date())
        elif command_input == '1':
            a.paths_update()
            a = stockupdate()
        elif command_input == 'db':
            a.dashboard_display()

main_start()