import pygsheets

file_path = "/home/rory/.tryhard_profile/nth-celerity-328105-4133fe1d85aa.json"
gc = pygsheets.authorize(service_file = file_path)
spread_sheet = gc.open("test1")
work_sheet = spread_sheet.worksheet_by_title("Aug_to_Dec")

cell_1 = work_sheet.cell("D2")
cell_1.color = (0.4,1,0.4,0.4)
