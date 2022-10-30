# Packages
# -----------------------------------------------------------------------
# pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi
# pip install xbbg
# pip install pynput
# -----------------------------------------------------------------------

# Documentation
# -----------------------------------------------------------------------
# https://xbbg.readthedocs.io/en/latest/
# -----------------------------------------------------------------------


# Needed for importing parent folder
# -----------------------------------------------------------------------
import os, sys
sys.path.insert(1, os.path.abspath('./src'))
#print(os.path.abspath('.'))
# -----------------------------------------------------------------------


#Paths
#--------------------------------------------------------------------------------------------------------
global path_output_folder;              path_output_folder = 'data'    
global path_remote_output_folder;       path_remote_output_folder = '//finnt11/qrm/Bloomberg'


global path_mkt_file;           path_mkt_file = 'data/query_bbg.xlsx'    

#global path_mkt_file_csv; path_mkt_file_csv = '_data/query_rates.csv'    


# Variables iniatilization
# -----------------------------------------------------------------------
global tickers_list
global PE_list

tickers_list =[
                        "FEDL01 Index",
                        "SOFRRATE Index",
                        "TSFR1M Index",
                        "TSFR3M Index",
                        "TSFR6M Index",
                        "TSFR12M Index",
                        "SOFR30A Index",
                        "SOFR90A Index",
                        "SOFR180A Index",
                        "US0001M Index",
                        "US0003M Index",
                        "US0006M Index",
                        "US0012M Index",
                        "BSBYON Index",
                        "BSBY1M Index",
                        "BSBY3M Index",
                        "BSBY6M Index",
                        "USSWAP2 Curncy",
                        "USSWAP3 Curncy",
                        "USSWAP4 Curncy",
                        "USSWAP5 Curncy",
                        "USSW6 Curncy",
                        "USSWAP7 Curncy",
                        "USSW8 Curncy",
                        "USSW9 Curncy",
                        "USSWAP10 Curncy",
                        "USSWAP20 Curncy",
                        "USSWAP30 Curncy",
                        "USOSFRC BGN Curncy",  #SOFR swap 3m
                        "USOSFRF BGN Curncy",  #SOFR swap 6m
                        "USOSFR1 BGN Curncy",
                        "USOSFR2 BGN Curncy",
                        "USOSFR3 BGN Curncy",
                        "USOSFR4 BGN Curncy",
                        "USOSFR5 BGN Curncy",	
                        "USOSFR6 BGN Curncy",
                        "USOSFR7 BGN Curncy",
                        "USOSFR8 BGN Curncy",
                        "USOSFR9 BGN Curncy",
                        "USOSFR10 BGN Curncy",
                        "USOSFR20 Curncy",
                        "USOSFR30 BGN Curncy",
                        "GT2 Govt",
                        "GT10 Govt",
                        "GT30 Govt",
                        "USSRVL1 Curncy",
                        "IBOV Index",
                        "BRL Curncy",
                        "BRAZIL CDS USD SR 5Y D14 Corp",
                        "ODF23 Comdty",
                        "ODF24 Comdty",
                        "ODF25 Comdty",
                        "ODF26 Comdty",
                        "ODF27 Comdty",
                        "ODF28 Comdty",
                        "ODF29 Comdty",
                        "ODF30 Comdty",
                        "ODF31 Comdty",
                        "ODF32 Comdty",
                        "ODF33 Comdty",
                        "ITUB4 BZ Equity",
                        "BBDC4 BZ Equity",
                        "CPI YOY Index",
                        "CPI XYOY Index",
                        "PCE CRCH Index",
                        "PCE CHNC Index",
                        "FAOFOODI Index",
                        "CL1 Comdty",
                        "SPX Index",
                        "CCMP Index",
                        "VIX Index",
                        "DXY Curncy",
                        "EUR Curncy",
                        "JPY Curncy",
                        "GBP Curncy",
                        "CDX IG CDSI GEN 5Y Corp",
                        "CDX HY CDSI GEN 5Y SPRD Corp",
                        "CDX EM CDSI GEN 5Y SPRD Corp",
                        "EHGDUS Index",
                        "EHGDUSY Index",
                        "EHUPUS Index",
                        "PRUSTOT Index",
                        "CRDSUI CDS EUR SR 5Y D14 Corp",
                        "LF55TRGU Index"
                        ]

PE_list = ['SPX Index','CCMP Index','IBOV Index']
# -----------------------------------------------------------------------


