import pandas as pd
import numpy as np
from openpyxl import load_workbook, Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

sheetname='transaction_level'

filename_1 = "qrm_market_value_and_exposure_derivatives_2021-12-31.xlsx"
filepath_1 = "./data/"  + filename_1

filename_2 = "qrm_market_value_and_exposure_derivatives_2021-12-31.xlsx"
filepath_2 = "./data/"  + filename_2

df_transactions_1 = pd.read_excel(filepath_1, sheet_name=sheetname, skiprows=8)  
df_transactions_2 = pd.read_excel(filepath_2, sheet_name=sheetname, skiprows=8)  

#identify exposures from new


#identify exposures from fixings


#identify exposures from matured


#identify exposures from amortizations, MTM, impact from rates