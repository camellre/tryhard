from stock_update import stockupdate
from get_date import get_date

def main_start():
    a = stockupdate()
    while True:
        if a.initiation == "yes":
            print("Data files are empty, initiation is needed.")
            while True:
                initiation_input_message = ('1.Google Service Account key path',
                    "2.Spreadsheet name",
                    "3.Worksheet name",
                    "4.item report file paths",
                    "5.shipment report file paths")
                print(*initiation_input_message)
                initiation_input = input("Please enter the command selection number:")
                if initiation_input == "exit":
                    break
                elif initiation_input not in ["1", "2", "3", "4", "5"]:
                    print("Selection is not valid.")
                    continue
                else:
                    a.paths_update()
            a = stockupdate()
        else:
            break

    a.dashboard_display()

    while True:
        command_input = input("Please enter the command selection number:")
        if command_input not in ["1", "2", "3", "db", 'exit']:
            print("Invalid input, please enter again.")
            continue
        elif command_input == 'exit':
            break
        elif command_input == '2':
            a.update_stock()
        elif command_input == '3':
            print(get_date())
        elif command_input == '1':
            a.paths_update()
        elif command_input == 'db':
            a.dashboard_display()


main_start()