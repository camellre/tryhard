from get_date import get_date
from stock_update import stock_update

def command_selection(selection_input = ''):
    switchers = {
        1: get_date,
    }
    try:
        return switchers.get(int(selection_input))()
    except (TypeError, ValueError):
        print("Command selection is not valid.")
        return None