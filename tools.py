import pandas

def stock_ticker_list():
    stock_list = pandas.read_csv("/home/yashas/Desktop/Quant/NET_NET/Equity.csv")
    stock_list=stock_list.transpose()
    ticker_list=stock_list.iloc[1]
    return ticker_list

def stock_security_list():
    stock_list = pandas.read_csv("/home/yashas/Desktop/Quant/NET_NET/Equity.csv")
    Security_Code_list = stock_list.index.to_list()
    return Security_Code_list

def sales_check(sales):#To check if last 5years of sales compounds at 12%
    sales_flag = 1
    for i in range(len(sales) - 1):
        sales[i]=str(sales[i])
        if "," in sales[i]:
            sales[i]=sales[i].replace(",","")
            
        if float(sales[i]) == 0:
            continue
        else:
            if ((float(sales[i + 1]) - float(sales[i])) / float(sales[i])) * 100 < 12:
                sales_flag = 0
                break
    return sales_flag

def OPMp_check(OPMp):#To check if OPMp>10% for last 5 yers
    OPMp_flag = 1
    for i in range(len(OPMp) - 1):
        OPMp[i] = str(OPMp[i]).replace("%", "")
        if "," in OPMp[i]:
            OPMp[i]=OPMp[i].replace(",","")
        if OPMp[i]=='nan':
            OPMp[i]=0    
        if float(OPMp[i]) < 10:
            OPMp_flag = 0
            break
    return OPMp_flag

def Stock_PtoE_check(stock_PtoE):#to check P/E<=20(currently)
    if "," in stock_PtoE:
        stock_PtoE=stock_PtoE.replace(",","")
    PtoE_flag = 0
    if stock_PtoE=="":
        PtoE_flag=0
    else:
        if float(stock_PtoE) <= 20:
            PtoE_flag = 1
    return PtoE_flag

def convert_to_number(number):
    if type(number)==int:
        return float(number)
    if type(number) == float:
        return number
    if "," in number:
        number=number.replace(",","")
    if ""==number:
        number=0
    if "NaN"==number:
        number=0
    return float(number)