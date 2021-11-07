def find_tracking(tracking_number_list = [], scanned_input = ''):
    if tracking_number_list == []:
        print("The tracking number data is not imported.")
        return None
    elif scanned_input == '':
        print("The input is empty.")
        return None
    else:
        try:
            tracking_output = 'Not Found!'
            scanned_input = scanned_input.upper()
            for i in range(len(tracking_number_list)):
                if scanned_input in tracking_number_list[i]:
                    tracking_output = tracking_number_list[i]
        except:
            print("The tracking number data or input is not valid.")
            return None
        else:
            return tracking_output
