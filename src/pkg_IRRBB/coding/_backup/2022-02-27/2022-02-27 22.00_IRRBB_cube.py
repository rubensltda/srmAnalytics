import pandas as pd


sheetname='2021-12-31'
filename = "qrm_market_value_and_exposure_derivatives_2021-12-31.xlsx"
filepath = "./data/"  + filename

df_loans = pd.read_excel(filepath, sheet_name=sheetname, skiprows=8, index_col=0)  

list_allocations = df_loans['Level 03.1'].unique()
list_indexes = df_loans['Level 03.3'].unique()
list_products = df_loans['Level 04'].unique()

print(list_allocations)
print(list_indexes)
print(list_products)

df_loans.to_excel("coding/output/validation.xlsx", sheet_name="transactions")