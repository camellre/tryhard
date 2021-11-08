import pandas as pd
import numpy as np
from input_data import input_data
from input_worksheet import input_worksheet
from command_selection import command_selection
from dashboard_display import dashboard_display
from read_paths import read_paths

#def main_start():  
profile_list = [0,1,2,3,4]
profile_output = list(map(read_paths,profile_list))

dashboard_display(profile_output[2], profile_output[3])

while True:
    command_input = input("Please enter the command selection number:")
    if command_input == 'exit':
        break
    elif command_selection(command_input) == None:
        continue
    else:
        command_selection(command_input)