profile_paths = [
    '/home/rory/.tryhard_profile/profile.txt',
    '/home/rory/.tryhard_profile/spreadsheet_names.txt',
    '/home/rory/.tryhard_profile/item_report_path.txt',
    '/home/rory/.tryhard_profile/shipment_report_path.txt',
    '/home/rory/.tryhard_profile/scanned_tracking.txt'
]

def read_paths(path_i):
    try:
        file_content_output = []
        with open(profile_paths[path_i], 'r') as f:
            file_content = f.readlines()
            for i in file_content:
                file_content_output.append(i[:-1])
    except:
        print("File path is not valid.")
        return None
    else:
        return file_content_output