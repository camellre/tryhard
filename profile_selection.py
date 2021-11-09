

class profile:
    profile_length = 10 #class static attribute regardless of instances
    profile_paths = [
        '/home/rory/.tryhard_profile/profile.txt',
        '/home/rory/.tryhard_profile/spreadsheet_names.txt',
        '/home/rory/.tryhard_profile/item_report_path.txt',
        '/home/rory/.tryhard_profile/shipment_report_path.txt',
        '/home/rory/.tryhard_profile/scanned_tracking.txt'
        ]
    def __init__(self, g_service_key, item_file, shipment_file, scanned_file):
        self.g_service_key = g_service_key
        self.item_file = item_file
        self.shipment_file = shipment_file
        self.scanned_file = scanned_file
    
    @classmethod
    def read_paths(cls, file_path):
        try:
            cls = []
            with open(file_path, 'r') as f:
                file_content = f.readlines()
                for i in file_content:
                    cls.append(i[:-1])
        except:
            print("File path is not valid.")
            return None
        else:
            return cls
    
print(profile.read_paths(profile.profile_paths[3]))