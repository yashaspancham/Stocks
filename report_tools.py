import pandas

def security_code_to_ticker_and_name(security_code):
    list_of_stocks=pandas.read_csv('/home/yashas/Desktop/Quant/NET_NET/Equity.csv')
    list_of_security_code=list(list_of_stocks.index)
    list_of_ticker=list(list_of_stocks['Issuer Name'])
    list_of_company_names=list(list_of_stocks['Security Code'])
    for i in range(len(list_of_security_code)):
        if(str(security_code)==str(list_of_security_code[i])):
            return list_of_ticker[i],list_of_company_names[i]
    print("Error,Security Code Not Found")
    return None,None
