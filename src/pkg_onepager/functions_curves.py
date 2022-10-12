# import config_module as config
# config.initialize()

def find_ticker_curve_by_tenor(curves_dict, curve_find, tenor_find):
    curve_ticker_list = curves_dict[curve_find][0]
    
    bool_found = 0
    
    i = 0
    while bool_found == 0 and i < len(curve_ticker_list):
        
        tenor = curve_ticker_list[i][0]
        if (tenor == tenor_find):
            ticker = curve_ticker_list[i][1]
            bool_found = 1
        i += 1
        #print(str(tenor) + str(ticker))
        
    if bool_found == 0:
        ticker = "N/A"
    
    return ticker


# for testing
#######################################################################################
# ticker = find_ticker_curve_by_tenor(config.ir_curves_dict, "Libor curve", 10)
# ticker = find_ticker_curve_by_tenor(config.ir_curves_dict, "SOFR curve", 2)
# print(ticker)


