
import pandas as pd
import numpy as np
from openpyxl import load_workbook, Workbook
from openpyxl.utils.dataframe import dataframe_to_rows




sheetname='transaction_level'
filename = "qrm_market_value_and_exposure_derivatives_2021-12-31.xlsx"
filepath = "./data/"  + filename

df_transactions = pd.read_excel(filepath, sheet_name=sheetname, skiprows=8)  

print(df_transactions)

###################################################################################
# import os
# cwd = os.getcwd()
# print("Current working directory: {0}".format(cwd))


###################################################################################
#df_transactions = pd.read_excel(filepath, sheet_name=sheetname, skiprows=8, index_col=0)  

###################################################################################
#df_transactions.to_excel("./output/validation2.xlsx", sheet_name="transactions")



####################################################################
# xlr = pd.ExcelWriter('./output/validation.xlsx')
# df_loans.to_excel(xlr, 'df_transactions')
# xlr.save()


#wb = load_workbook(filename = filepath)

