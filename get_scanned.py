
def get_scanned(scanned_tracking_path = ''):
    if scanned_tracking_path == '':
        print('Scanned tracking file path is empty.')
        return None
    else:
        scanned_tracking_filtered = []
        try:
            with open(scanned_tracking_path, 'r') as scanned_tracking_number:
                scanned_tracking_number_list = scanned_tracking_number.readlines()
                for i in scanned_tracking_number_list:
                    scanned_tracking_filtered.append(i[:-1])
        except:
            print("Scanned tracking number data is not valid.")
            return None
        else:
            return scanned_tracking_filtered
    