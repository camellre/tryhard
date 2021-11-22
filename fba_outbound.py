import pandas as pd
import numpy as np
import pygsheets
from get_date import get_date

class fba_outbound():
    def __init__(self, found_order):
        self.found_order = found_order
        self.item_name = ''
        self.item_asin = ''
        self.item_quantity = ''
        self.item_condition = ''
        self.item_weight = ''
        self.item_dimension = ''
        self.item_cost = ''