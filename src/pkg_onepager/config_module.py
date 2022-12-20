# Pending to code
# -----------------------------------------------------------------------
# enviar do email BID: 
# criar usuario generico / lista distribuicao
# criar thread para mandar email
# deploy in BBG machine
# rotina para nao deixar bloomberg deslogar
# crirar metodo mais rapido para serie shiftada
# percentile in curves statistics
# criar e mostrar series SOFR 5bd e 15bg (according to NSG ALCO material)
# github secure
# cortando final do italico: faltando espaco na coluna? ou colocar gif na funcao utils?
# -----------------------------------------------------------------------


# Packages
# -----------------------------------------------------------------------
# python -m venv venv

# pip install pandas
# pip install matplotlib
# pip install openpyxl
# pip install scipy (for interpolation)
# pip install schedule
# -----------------------------------------------------------------------


# Needed for importing parent folder
# -----------------------------------------------------------------------
# import os, sys
# sys.path.insert(1, os.path.abspath('./src'))
# print(os.path.abspath('.'))
# -----------------------------------------------------------------------
import datetime as dt
import pkg_common.utils as ut
from dateutil.relativedelta import relativedelta

def initialize():
    
    #Dates variables
    #--------------------------------------------------------------------------------------------------------
    global today_dt;           today_dt = dt.date.today()
    #global today_dt;            today_dt = dt.date(2022, 10, 27) # for testing             
    
    global this_EOQ_dt;         this_EOQ_dt = ut.find_quarter_end(today_dt)
    global previous_dt;         previous_dt = ut.find_previous_day(today_dt)
    global last_EOW_dt;         last_EOW_dt = ut.find_previous_friday(today_dt)
    global last_EOM_dt;         last_EOM_dt = today_dt.replace(day=1) - dt.timedelta(days=1)
    global last_EOQ_dt;         last_EOQ_dt = ut.find_quarter_end(today_dt,-1)
    global last_EOY_dt;         last_EOY_dt = dt.date(today_dt.year-1, 12, 31) 
    global last_1m_dt;          last_1m_dt = today_dt + relativedelta(months=-1)
    global last_3m_dt;          last_3m_dt = today_dt + relativedelta(months=-3)
    global last_12m_dt;         last_12m_dt = today_dt + relativedelta(months=-12)
    global last_5y_dt;          last_5y_dt = today_dt + relativedelta(years=-5)
    global last_10y_dt;         last_10y_dt = today_dt + relativedelta(years=-10)
    global last_EOQ_back8_dt;   last_EOQ_back8_dt = ut.find_quarter_end(today_dt,-8)
    global next_EOQ_fwd1_dt;    next_EOQ_fwd1_dt = ut.find_quarter_end(today_dt,1)
    global next_EOY_dt;         next_EOY_dt = dt.date(today_dt.year, 12, 31) 

    
    #Email config
    #--------------------------------------------------------------------------------------------------------
    global send_email_flag;      send_email_flag = True
    #global send_email_flag;       send_email_flag = False
    
    global send_email_idb;        send_email_idb = True
    #global send_email_idb;        send_email_idb = False
    
    # global email_internal_srm_list;     email_internal_srm_list = ["rubensh@iadb.org"]
    # global email_distribution_list;     email_distribution_list = ["rubensh@iadb.org","bloomrmp@iadb.org"]    
    
    global email_internal_srm_list;     email_internal_srm_list = ["sylviag@iadb.org","rubensh@iadb.org"]
    global email_distribution_list;     email_distribution_list = ["sylviag@iadb.org","rubensh@iadb.org","fruizgarcia@iadb.org","fin-alm@iadb.org"]    


    #Assets and groups dictionaries
    #--------------------------------------------------------------------------------------------------------
    global assets_dict;
    assets_dict = { 
                    "Fed Funds": ["FEDL01 Index","Rate","tan","-"],
                    "SOFR O/N": ["SOFRRATE Index","Rate","blue","-"],
                    "Libor 1M": ["US0001M Index","Rate","tan","-"],
                    "Libor 3M": ["US0003M Index","Rate","darkorange","-"],
                    "Libor 6M": ["US0006M Index","Rate","goldenrod","-"],
                    "Libor 12M": ["US0012M Index","Rate","orange","-"],
                    "SOFR 90d comp.": ["SOFR90A Index","Rate","blue","-"],
                    "SOFR 180d comp.": ["SOFR180A Index","Rate","indigo","-"],
                    "SOFR Term 1M": ["TSFR1M Index","Rate","thistle","-"],
                    "SOFR Term 3M": ["TSFR3M Index","Rate","darkviolet","-"],
                    "SOFR Term 6M": ["TSFR6M Index","Rate","indigo","-"],
                    "SOFR Term 12M": ["TSFR12M Index","Rate","slateblue","-"],
                    "BSBY O/N": ["BSBYON Index","Rate","gold","-"],
                    "BSBY1M Index": ["BSBY1M Index","Rate","khaki","-"],
                    "BSBY3M Index": ["BSBY3M Index","Rate","beige","-"],
                    "BSBY6M Index": ["BSBY6M Index","Rate","yellow","-"],
                    "Treasury 2Y": ["GT2 Govt","Rate","salmon","-"],
                    "Treasury 10Y": ["GT10 Govt","Rate","tomato","-"],
                    "Treasury 30Y": ["GT30 Govt","Rate","rosybrown","-"],
                    "Libor Swap 2Y": ["USSWAP2 Curncy","Rate","limegreen","-"],
                    "Libor Swap 5Y": ["USSWAP5 Curncy","Rate","forestgreen","-"],
                    "Libor Swap 10Y": ["USSWAP10 Curncy","Rate","lightseagreen","-"],
                    "Libor Swap 30Y": ["USSWAP30 Curncy","Rate","seagreen","-"],
                    "SOFR Swap 2Y": ["USOSFR2 BGN Curncy","Rate","limegreen","-"],
                    "SOFR Swap 5Y": ["USOSFR5 BGN Curncy","Rate","forestgreen","-"],
                    "SOFR Swap 10Y": ["USOSFR10 BGN Curncy","Rate","lightseagreen","-"],
                    "SOFR Swap 30Y": ["USOSFR30 BGN Curncy","Rate","seagreen","-"],
                    "Market Basis Swap - Libor 3M vs SOFR Basis": ["USSRVL1 Curncy decimals","Rate_Spread","lightcoral","-"],
                    "Libor 3M (shifted)": ["US0003M Index_90d_back","Rate","darkorange","--"],
                    "Libor 6M (shifted)": ["US0006M Index_180d_back","Rate","darkorange","--"],
                    "SOFR Term 3M (shifted)": ["TSFR3M Index_90d_back","Rate","darkviolet","--"],
                    "SOFR Term 6M (shifted)": ["TSFR6M Index_180d_back","Rate","darkviolet","--"],
                    "Spread: Libor 3M - Sofr Term 3M": ["Spread_Libor3M_Sofr3MTerm","Rate_Spread","dimgray","-"],
                    "Spread: Libor 3M (shifted) - SOFR 90d comp.": ["Spread_Libor3Mshifted_SOFR90dcomp","Rate_Spread","dimgray","-"],
                    "Spread: Libor 6M (shifted) - SOFR 180d comp.": ["Spread_Libor6Mshifted_SOFR180dcomp","Rate_Spread","dimgray","-"],
                    "Spread: SOFR Term 3M (shifted) - Sofr 90d comp.": ["Spread_SOFRT3Mshifted_SOFR90dcomp","Rate_Spread","dimgray","-"],
                    "Spread: SOFR Term 6M (shifted) - Sofr 180d comp.": ["Spread_SOFRT6Mshifted_SOFR180dcomp","Rate_Spread","dimgray","-"],
                    "Spread: Treasury 10Y - Treasury 2Y": ["Spread_T2_10","Rate_Spread","dimgray","-"],
                    "Ibovespa":["IBOV Index","Price_0d","orange","-"],
                    "Brazilian Real":["BRL Curncy","Price_4d","green","-"],
                    "Brazil 5Y CDS":["BRAZIL CDS USD SR 5Y D14 Corp","Rate_0d","gray","-"],
                    "BRL PRE 2Y": ["ODF24 Comdty","Rate","indigo","-"],
                    "BRL PRE 5Y": ["ODF27 Comdty","Rate","darkviolet","-"],
                    "BRL PRE 10Y": ["ODF33 Comdty","Rate","blue","-"],
                    "ITUB4": ["ITUB4 BZ Equity","Price","Orange","-"],
                    "BBDC4": ["BBDC4 BZ Equity","Price","Red","-"],
                    "CPI YOY": ["CPI YOY Index","Rate","Black","-"],
                    "CORE CPI YOY": ["CPI XYOY Index","Rate","Black","-"],
                    "US Personal Consumption Expenditures - Nominal": ["PCE CRCH Index","Rate","Black","-"],
                    "US Personal Consumption Expenditures - Real"   : ["PCE CHNC Index","Rate","Blue","--"],
                    "UN Food and Agriculture World Food Price Index": ["FAOFOODI Index","Price","Black","-"],
                    "OIL CME Futures": ["CL1 Comdty","Price","Black","-"],
                    "S&P500": ["SPX Index","Price_0d","Blue","-"],
                    "NASDAQ": ["CCMP Index","Price_0d","Orange","-"],
                    "S&P500 P/E": ["USPESPPE Index","Price","Blue","--"],
                    "VIX": ["VIX Index","Price","Red","-"],
                    "CDX North America High Yield Index": ["CDX HY CDSI GEN 5Y SPRD Corp","Price","Green","-"],
                    "CDX North America Investment Grade Index": ["CDX IG CDSI GEN 5Y Corp","Price","Green","-"],
                    "CDX Markit Emerging Markets Index": ["CDX EM CDSI GEN 5Y SPRD Corp","Price","Green","-"],
                    "Dollar Index": ["DXY Curncy","Price","Green","-"],
                    "EUR/USD": ["EUR Curncy","Price_4d","Green","-"],
                    "GBP/USD": ["GBP Curncy","Price_4d","Green","-"],
                    "JPY/USD": ["JPY Curncy","Price","Green","-"],
                    "USD Real GDP QoQ": ["EHGDUS Index","Rate","Black","-"],
                    "USD Real GDP YoY": ["EHGDUSY Index","Rate","Black","-"],
                    "US Unemployment Rate": ["EHUPUS Index","Rate","Black","-"],
                    "US Participation Rate": ["PRUSTOT Index","Price","Black","-"],
                    "S&P500 Forward P/E": ["SPX Index_PE_forward","Price","Black","-"],
                    "S&P500 Trailing P/E": ["SPX Index_PE_trailing","Price","Gray","-"],
                    "NASDAQ Forward P/E": ["CCMP Index_PE_forward","Price","Black","-"],
                    "NASDAQ Trailing P/E": ["CCMP Index_PE_trailing","Price","Gray","-"],
                    "IBOV Forward P/E": ["IBOV Index_PE_forward","Price","Black","-"],
                    "IBOV Trailing P/E": ["IBOV Index_PE_trailing","Price","Gray","-"],
                    "Credit Suisse CDS": ["CRDSUI CDS EUR SR 5Y D14 Corp","Price","Green","-"],
                    "Bloomberg UK Gilt 15+ TR value unhedged GBP": ["LF55TRGU Index","Price","Green","-"],
                }
    


    global groups_dict;
    groups_dict = { 
                    "Risk-free rates": ["Fed Funds","SOFR O/N"], 
                    "LIBOR": ["Libor 1M","Libor 3M","Libor 6M","Libor 12M"], 
                    "SOFR TERM": ["SOFR Term 1M","SOFR Term 3M", "SOFR Term 6M", "SOFR Term 12M"],
                    "SOFR Average": ["SOFR 90d comp.","SOFR 180d comp."],
                    "BSBY": ["BSBY O/N","BSBY1M Index", "BSBY3M Index", "BSBY6M Index"],
                    "LIBOR Swaps": ["Libor Swap 2Y","Libor Swap 5Y", "Libor Swap 10Y"],
                    "SOFR Swaps": ["SOFR Swap 2Y","SOFR Swap 5Y", "SOFR Swap 10Y"],
                    "Treasuries": ["Treasury 2Y","Treasury 10Y", "Treasury 30Y"],
                    "BRL PRE": ["BRL PRE 2Y","BRL PRE 5Y", "BRL PRE 10Y"],
                    "Libor 3M (shifted) vs SOFR 90d comp.": ["Libor 3M (shifted)","SOFR 90d comp."],
                    "Libor 6M (shifted) vs SOFR 180d comp.": ["Libor 6M (shifted)","SOFR 180d comp."],
                    "SOFR Term 3M (shifted) vs SOFR 90d comp. (SOFR Term as a predictor)": ["SOFR Term 3M (shifted)","SOFR 90d comp."],
                    "SOFR Term 6M (shifted) vs SOFR 180d comp. (SOFR Term as a predictor)": ["SOFR Term 6M (shifted)","SOFR 180d comp."],
                    "Libor 3M vs SOFR Term 3M (Credit component)": ["Libor 3M","SOFR Term 3M"],
                    "Market Basis Swap pricing": ["Market Basis Swap - Libor 3M vs SOFR Basis","Spread: Libor 3M - Sofr Term 3M"],
                    "Brazil Stocks": ["ITUB4","BBDC4"],
                    "BRL PRE": ["BRL PRE 5Y","BRL PRE 10Y"],
                    "IBOV P/E": ["IBOV Forward P/E","IBOV Trailing P/E"],
                    "S&P500 P/E": ["S&P500 Forward P/E","S&P500 Trailing P/E"],
                    "NASDAQ P/E": ["NASDAQ Forward P/E","NASDAQ Trailing P/E"],
                    "US Personal Consumption Expenditures MOM": ["US Personal Consumption Expenditures - Real","US Personal Consumption Expenditures - Nominal"]
                  }
    
    
    global ir_curves_dict;
    ir_curves_dict = {
                      "LIBOR YC":[ [  
                                      (0.25,"US0003M Index"),
                                      (0.5,"US0006M Index"),
                                      (1,"US0012M Index"),
                                      (2,"USSWAP2 Curncy"),
                                      (3,"USSWAP3 Curncy"),
                                      (4,"USSWAP4 Curncy"),
                                      (5,"USSWAP5 Curncy"),
                                      (6,"USSW6 Curncy"),
                                      (7,"USSWAP7 Curncy"),
                                      (8,"USSW8 Curncy"),
                                      (9,"USSW9 Curncy"),
                                      (10,"USSWAP10 Curncy"),
                                      (20,"USSWAP20 Curncy"),
                                      (30,"USSWAP30 Curncy")
                                    ]
                                    ,'green'
                                  ]
                      ,
                      "SOFR YC":[  [
                                    (0.25,"USOSFRC BGN Curncy"),
                                    (0.5,"USOSFRF BGN Curncy"),
                                    (1,"USOSFR1 BGN Curncy"),
                                    (2,"USOSFR2 BGN Curncy"),
                                    (3,"USOSFR3 BGN Curncy"),
                                    (4,"USOSFR4 BGN Curncy"),
                                    (5,"USOSFR5 BGN Curncy"),
                                    (6,"USOSFR6 BGN Curncy"),
                                    (7,"USOSFR7 BGN Curncy"),
                                    (8,"USOSFR8 BGN Curncy"),
                                    (9,"USOSFR9 BGN Curncy"),
                                    (10,"USOSFR10 BGN Curncy"),
                                    (20,"USOSFR20 Curncy"),
                                    (30,"USOSFR30 BGN Curncy")
                                    ]
                                    ,'blue'
                                ]
                    ,
                    "BRL PRE":[  [(1,"ODF23 Comdty"),
                                  (2,"ODF24 Comdty"),
                                  (3,"ODF25 Comdty"),
                                  (4,"ODF26 Comdty"),
                                  (5,"ODF27 Comdty"),
                                  (6,"ODF28 Comdty"),
                                  (7,"ODF29 Comdty"),
                                  (8,"ODF30 Comdty"),
                                  (9,"ODF31 Comdty"),
                                  (10,"ODF33 Comdty")
                                  ]
                                  ,'blue'
                              ]
                    }
    
