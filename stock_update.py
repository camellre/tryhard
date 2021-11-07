from find_order import find_order
from play_sound import play_sound
from get_date import get_date

def stock_update(shipment_tracking_number_list, shipment_tracking_number, item_info, work_sheet, scanned_tracking_number):
    
    while True:
        row_0 = input('Please enter the beginning row number where it should start:')
        if row_0 == '':
            print('The beginning row must be entered.')
            continue
        elif row_0 == 'exit':
            return None
        else:
            row = int(row_0)
            break

    scanned_tracking_number_list = scanned_tracking_number

    while True:
        
        a = input('Please scan tracking number:')
        a = a.upper()
        if a == 'EXIT':
            break
        elif a == '':
            print('The tracking number must be scanned.')
            continue
        elif a != '' and a != 'EXIT':
            b = find_order(a, shipment_tracking_number_list, shipment_tracking_number, item_info)
            if b == "Not Found!":
                if a in scanned_tracking_number_list:
                    print('Already scanned.')
                    continue
                else:
                    scanned_tracking_number_list.append(a)
                    print("Not Found!")
                    play_sound(exceptions = 'not_found')
                    work_sheet.update_value('A{}'.format(row), get_date())
                    work_sheet.update_value('K{}'.format(row), a)
                    row += 1
                    continue
                
            elif b == []:
                if a in scanned_tracking_number_list:
                    print('Already scanned.')
                    continue
                else:
                    scanned_tracking_number_list.append(a)
                    print("Tracking number is not valid or order is too old.")
                    play_sound(exceptions = 'not_found')
                    work_sheet.update_value('A{}'.format(row), get_date())
                    work_sheet.update_value('K{}'.format(row), a)
                    row += 1
                    continue

            else:
                if a in scanned_tracking_number_list:
                    print('Already scanned.')
                    continue
                else:
                    scanned_tracking_number_list.append(a)
                    print(b)
                    for i in range(len(b)):
                        play_sound(numbers = str(b[i][8]), conditions = str(b[i][4]))
                        work_sheet.update_value('A{}'.format(row), get_date())
                        work_sheet.update_row(row, b[i], col_offset=1)
                        row += 1

    with open('/home/rory/Inventory-Management-main/scanned_tracking_number.txt', 'a') as output_file:
        for item in scanned_tracking_number_list:
            output_file.write(item + '\n')