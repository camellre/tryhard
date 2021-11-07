def dashboard_display(item_report_files_paths = [], shipment_data_files_paths = []):
    message = ("########## Dashboard ##########",
        "1.Data Files Paths Update",
        "Current Item Report file path:",
        "\n".join(item_report_files_paths),
        "\nCurrent shipment_data_files_paths:",
        "\n".join(shipment_data_files_paths),
        "\n2.Google Service Account Key Update.",
        "\n3.Spreadsheet and Worksheet Name Update",
        "\n4.Daily Incoming Stock Update.",
        "\n5.Show the date of today.")
    
    print(*message, sep = '\n')