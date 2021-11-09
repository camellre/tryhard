import pandas as pd
import numpy as np
from command_selection import command_selection
from dashboard_display import dashboard_display
from profile_selection import profile

def main_start():
    current_profile = profile()
    dashboard_display(current_profile.item_file, current_profile.shipment_file)
    while True:
        command_input = input("Please enter the command selection number:")
        if command_input == 'exit':
            break
        elif command_selection(command_input) == None:
            continue
        else:
            command_selection(command_input)

main_start()