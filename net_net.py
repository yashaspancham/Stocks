import pandas
import numpy
import time
from bs4 import BeautifulSoup

start_time=time.time()
stock_list=pandas.read_csv("/home/yashas/Desktop/Quant/NET_NET/Equity.csv")
security_code_list=list(stock_list.index.tolist())
count=0#keeps track of number of stocks processed
problem_count=0
vaule_stock_found=0
value_stocks=[]

for security_code in security_code_list:
    if count==1000000:
        end_time=time.time()
        print(f"The number of stocks: {count}")
        print(f"Total time={end_time-start_time}seconds")
        print(f"The selected stocks are: {value_stocks}")
        print(f"selected number of stocks: {vaule_stock_found}")
        print(f"Number of stocks unable to process: {problem_count}")
        exit(0)
    try:
        equity=pandas.read_html("/home/yashas/Desktop/Quant/NEW_DATA/"+str(security_code)+".html")
        BalanceSheet=equity[6]
        BalanceSheet=pandas.DataFrame(BalanceSheet)
        BalanceSheet=BalanceSheet.transpose()
        total_liabalitiles=list(BalanceSheet[4])
        total_liabalitiles=total_liabalitiles[-1]
        total_liabalitiles=str(total_liabalitiles)
        total_liabalitiles=total_liabalitiles.replace(",","")
        if total_liabalitiles is numpy.NAN or total_liabalitiles=="":
            total_liabalitiles=0
        total_liabalitiles=float(total_liabalitiles)
        Current_assets=list(BalanceSheet[8])
        Current_assets=Current_assets[-1]
        Current_assets=str(Current_assets)
        Current_assets=Current_assets.replace(",","")
        if Current_assets is numpy.NAN or Current_assets=="":
            Current_assets="0"
        Current_assets=float(Current_assets)
        with open("/home/yashas/Desktop/Quant/NEW_DATA/"+str(security_code)+".html") as file:
            html_content=file.read()
        soup=BeautifulSoup(html_content,"html.parser")
        market_cap = soup.find('li', class_='flex flex-space-between')
        market_cap_text = market_cap.text#to obtain market cap
        market_cap_text=market_cap_text.replace("\n","")
        market_cap_text=market_cap_text.replace(" ","")
        market_cap_text=market_cap_text.replace("MarketCap₹","")
        market_cap_text=market_cap_text.replace("Cr.","")
        market_cap_text=market_cap_text.replace(",","")
        if market_cap_text=="" or market_cap_text=="NaN":
            market_cap_text=0
        market_cap_text=float(market_cap_text)
        intrinsic_value=float((9/10)*(Current_assets-total_liabalitiles))
        print(security_code,intrinsic_value,Current_assets,total_liabalitiles)
        if market_cap_text<intrinsic_value:
            value_stocks.append(security_code)
            vaule_stock_found+=1
    except Exception:
        print(f"Unable to process: {security_code}")
        print("Error "+str(type(Exception)))
        problem_count+=1
    count+=1

end_time=time.time()
print(f"The number of stocks: {count}")
print(f"Total time={end_time-start_time}seconds")
print(f"The selected stocks are: {value_stocks}")
print(f"selected number of stocks: {vaule_stock_found}")
print(f"Number of stocks unable to process: {problem_count}")