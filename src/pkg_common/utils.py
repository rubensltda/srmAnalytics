import datetime as dt
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter
import math

def format_date(dt):
    dt_suffix = ''
    dic = { '01':'st','21':'st','31':'st', 
            '02':'nd','22':'nd', 
            '03':'rd','23':'rd'
            }
    
    try: 
        dt_suffix = dic[dt.strftime("%d")]
    except KeyError:
        dt_suffix = 'th'

    dt_formatted = dt.strftime("%b %#d")
    dt_formatted = dt_formatted 
    
    str_dt_formatted = str(dt_formatted) + dt_suffix + ", " + str(dt.strftime("%Y"))

    return str_dt_formatted

def format_date_short(dt):
    dt_suffix = ''
    dic = { '01':'st','21':'st','31':'st', 
            '02':'nd','22':'nd', 
            '03':'rd','23':'rd'
            }
    
    try: 
        dt_suffix = dic[dt.strftime("%d")]
    except KeyError:
        dt_suffix = 'th'

    dt_formatted = dt.strftime("%b %#d")
    dt_formatted = dt_formatted 
    
    str_dt_formatted = str(dt_formatted) + dt_suffix + ", " + str(dt.strftime("%y"))

    return str_dt_formatted

def format_date_compact(dt):
    dt_formatted = dt.strftime("%b %#d")
    dt_formatted = dt_formatted 
    
    str_dt_formatted = str(dt_formatted)
    return str_dt_formatted



def find_previous_day(today_dt):
    previous_dt =  today_dt - dt.timedelta(days=1)
    return previous_dt

def find_previous_friday(today_dt):
    last_EOW_dt = today_dt
    if last_EOW_dt.weekday() == 4:
        last_EOW_dt -=  dt.timedelta(days=7)
    else:
        while last_EOW_dt.weekday() != 4:
            last_EOW_dt -=  dt.timedelta(days=1)
    return last_EOW_dt

def find_previous_quarter_date(today_dt):
    date_month = today_dt.month
    date_year = today_dt.year
    
    if date_month == 1 or date_month == 2 or date_month == 3:
        last_EOQ_dt = dt.date(date_year-1, 12, 31)
    elif date_month == 4 or date_month == 5 or date_month == 6:
        last_EOQ_dt = dt.date(date_year, 3, 31)
    elif date_month == 7 or date_month == 8 or date_month == 9:
        last_EOQ_dt = dt.date(date_year, 6, 30)
    else:
        last_EOQ_dt = dt.date(date_year, 9, 30)
    
    return last_EOQ_dt

def find_next_quarter_date(today_dt):
    date_month = today_dt.month
    date_year = today_dt.year
    
    if date_month == 1 or date_month == 2 or date_month == 3:
        next_EOQ_dt = dt.date(date_year, 3, 31)
    elif date_month == 4 or date_month == 5 or date_month == 6:
        next_EOQ_dt = dt.date(date_year, 6, 30)
    elif date_month == 7 or date_month == 8 or date_month == 9:
        next_EOQ_dt = dt.date(date_year, 9, 30)
    else:
        next_EOQ_dt = dt.date(date_year, 12, 31)

    return next_EOQ_dt

def find_quarter_end(date_input, shift=0):
    quarter_end = date_input
    
    if shift > 0:
        quarter_end = find_next_quarter_date(quarter_end + dt.timedelta(days=1))    
        while shift != 0:
            quarter_end = find_next_quarter_date(quarter_end + dt.timedelta(days=1))    
            shift -= 1
    elif shift < 0:
        while shift != 0:
            quarter_end = find_previous_quarter_date(quarter_end)    
            shift += 1
    else:
        quarter_end = find_next_quarter_date(date_input)    
    
    return quarter_end

def find_previous_JAJO(date_input):
    previous_JAJO = date_input
    date_day = date_input.day
    date_month = date_input.month
    date_year = date_input.year
    
    if (date_input >= dt.date(date_year, 1, 15)) and (date_input < dt.date(date_year, 4, 15)):
        previous_JAJO = dt.date(date_year, 1, 15)
    elif  (date_input >= dt.date(date_year, 4, 15)) and (date_input < dt.date(date_year, 7, 15)):
        previous_JAJO = dt.date(date_year, 4, 15)
    elif  (date_input >= dt.date(date_year, 7, 15)) and (date_input < dt.date(date_year, 10, 15)):
        previous_JAJO = dt.date(date_year, 7, 15)
    elif (date_input >= dt.date(date_year, 10, 15)):
        previous_JAJO = dt.date(date_year, 10, 15)
    else:
        previous_JAJO = dt.date(date_year-1, 10, 15)
    return previous_JAJO


def find_next_JAJO(date_input):
    next_JAJO = date_input
    date_day = date_input.day
    date_month = date_input.month
    date_year = date_input.year
    
    if (date_input > dt.date(date_year, 1, 15)) and (date_input <= dt.date(date_year, 4, 15)):
        next_JAJO = dt.date(date_year, 4, 15)
    elif  (date_input > dt.date(date_year, 4, 15)) and (date_input <= dt.date(date_year, 7, 15)):
        next_JAJO = dt.date(date_year, 7, 15)
    elif  (date_input > dt.date(date_year, 7, 15)) and (date_input <= dt.date(date_year, 10, 15)):
        next_JAJO = dt.date(date_year, 10, 15)
    elif  (date_input <= dt.date(date_year, 1, 15)):
        next_JAJO = dt.date(date_year, 1, 15)
    else:
        next_JAJO = dt.date(date_year+1, 1, 15)
    return next_JAJO


def format_quote(quote, quote_type='rate'):
    formatted_rate = ""
    quote_type = quote_type.upper()
    
    try:
        if quote_type=='RATE' or quote_type=='RATE_SPREAD':
            formatted_rate =  "{:,.2f}".format(quote)
        elif quote_type=='RATE_0D':
            formatted_rate =  "{:,.0f}".format(quote)
        elif quote_type=='PRICE':
            formatted_rate =  "{:,.2f}".format(quote)
        elif quote_type=='PRICE_0D':
            formatted_rate =  "{:,.0f}".format(quote)
        elif quote_type=='PRICE_4D':
            formatted_rate =  "{:,.4f}".format(quote)
        elif quote_type=='TRUNC':
            formatted_rate = "{:,.2f}".format(math.trunc(quote*100)/100)
        else:
            formatted_rate =  quote
    except:
        formatted_rate = quote
    
    return formatted_rate

def format_notional(amount):
    formatted_amount = ""
    try:
        formatted_amount =  "{:,.0f}".format(amount)
    except:
        formatted_amount = amount
    return formatted_amount



def format_axis_label(ticker_quote_type):
    quote_type = ticker_quote_type.upper()
    
    if quote_type == 'RATE':
         axis_formatter = FormatStrFormatter('%.2f')
    elif quote_type == 'RATE_0D':
        axis_formatter = FormatStrFormatter('%.0f')
    elif quote_type == 'PRICE_2D':
        axis_formatter = StrMethodFormatter('{x:,.2f}')
    elif quote_type == 'PRICE_0D':
        axis_formatter = StrMethodFormatter('{x:,.0f}')
    elif quote_type == 'PRICE_4D':
        axis_formatter = StrMethodFormatter('{x:,.4f}')
    else:
        axis_formatter = FormatStrFormatter('%.2f')
    return axis_formatter
    
    try:
        if quote_type=='RATE' or quote_type=='RATE_SPREAD':
            formatted_rate =  "{:,.2f}".format(quote)
        elif quote_type=='RATE_0D':
            formatted_rate =  "{:,.0f}".format(quote)
        elif quote_type=='PRICE':
            formatted_rate =  "{:,.2f}".format(quote)
        elif quote_type=='PRICE_0D':
            formatted_rate =  "{:,.0f}".format(quote)
        elif quote_type=='PRICE_4D':
            formatted_rate =  "{:,.4f}".format(quote)
        else:
            formatted_rate =  quote
    except:
        formatted_rate = quote
    
    return formatted_rate



def calculate_change(rate1, rate2):
    change_rate = ''
    try:
        change_rate = rate1 - rate2
    except:
        change_rate = '-'
    return change_rate

def calculate_change_pct(rate1, rate2):
    change_rate = ''
    try:
        change_rate = (rate1/rate2-1)*100
    except:
        change_rate = '-'
    return change_rate



def format_change_html(spread_px, quote_type='rate'):
    html_spread = ''

    try:
        if 'RATE' in quote_type.upper():
            spread_str = format_quote(spread_px,quote_type)
        else:
            spread_str = str("{:,.2f}".format(spread_px,quote_type)) + '%'
            
        if spread_px == 0: 
            html_spread = "<i>-&nbsp;&nbsp;&nbsp;</i>"
        elif spread_px > 0: 
            html_spread = f"<font color='green'><i>+{spread_str}</i></font>"
        else: 
            html_spread = f"<font color='red'><i>{spread_str}</i></font>"
    except:
        html_spread = spread_px
    return html_spread


def format_change_html_small(spread_px, quote_type='rate'):
    html_spread = ''
    
    try:
        if 'RATE' in quote_type.upper():
            spread_str = format_quote(spread_px,quote_type)
        else:
            spread_str = str("{:,.2f}".format(spread_px,quote_type)) + '%'
        
        
        if spread_px == 0: 
            html_spread = "<i>-&nbsp;&nbsp;</i>"
        elif spread_px > 0: 
            html_spread = f"<i><font color='green' size='1'>&nbsp;+{spread_str}</font></i>"
        else: #<0
            html_spread = f"<i><font color='red'  size='1'>&nbsp;{spread_str}</font><i>"
    except:
         html_spread = spread_px
    
    return html_spread


def get_parameters(param_find=0):
    param = ''
    try:
        with open('parameters.txt') as f:
            #lines = f.readlines()
            readline=f.read().splitlines()
        param = readline[param_find]
    except:
        print('Could not find parameter.')
        param = ''

    return param



