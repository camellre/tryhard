def dashboard_display(item_report_files_paths = [], shipment_data_files_paths = []):
    message = ("########## Dashboard ##########",
        "1.Data Files Paths Update",
        "Current Item Report file path:",
        "\n".join(item_report_files_paths),
        "Current shipment_data_files_paths:",
        "\n".join(shipment_data_files_paths),
        "2.Google Service Account Key Update.",
        "3.Spreadsheet and Worksheet Name Update",
        "4.Daily Incoming Stock Update.",
        "5.Show the date of today.")
    
    print(*message, sep = '\n')