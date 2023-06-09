import pandas
import requests
import csv
import time
from bs4 import BeautifulSoup
start_time=time.time()
#ticker="ITC"
#print(ticker)
stock_list=pandas.read_csv("/home/yashas/Desktop/Quant/NET_NET/Equity.csv")
ticker_list=list(stock_list["Issuer Name"])
#print(ticker_list)
count=0#keeps track of number of stocks processed
problem_count=0
vaule_stock_found=0
added_to_file=0
for ticker in ticker_list:
    if count==10:
        end_time=time.time()
        total_time=end_time-start_time
        print(f"total time={total_time}s")
        print(f"process faild={problem_count}stocks")
        print(f"total processed={count}stocks")
        print(f"Total value stocks found={vaule_stock_found}")
        print(f"Added to file:{added_to_file}stocks")
        exit(0)
    try:
        address="https://www.screener.in/company/"+ticker+"/"
        #print(address)
        equity=pandas.read_html(address)
        BalanceSheet=equity[6]
        BalanceSheet=pandas.DataFrame(BalanceSheet)
        BalanceSheet=BalanceSheet.transpose()
        #print(BalanceSheet[8])
        total_liabalitiles=list(BalanceSheet[4])
        total_liabalitiles=total_liabalitiles[-1]
        total_liabalitiles=int(total_liabalitiles)
        Current_assets=list(BalanceSheet[8])
        Current_assets=Current_assets[-1]
        Current_assets=int(Current_assets)
        #print(equity)
        # Create a request object to the web page.
        request = requests.get(address)
        # Use the `BeautifulSoup` library to parse the response.
        soup = BeautifulSoup(request.content, 'html.parser')
        # Find the element you want to scrape.
        market_cap = soup.find('li', class_='flex flex-space-between')
        # Extract the data from the element.
        market_cap_text = market_cap.text#to obtain market cap
        market_cap_text=market_cap_text.replace("\n","")
        market_cap_text=market_cap_text.replace(" ","")
        market_cap_text=market_cap_text.replace("MarketCap₹","")
        market_cap_text=market_cap_text.replace("Cr.","")
        market_cap_text=market_cap_text.replace(",","")
        market_cap_text=int(market_cap_text)
        in_value=(9/10)*(Current_assets-total_liabalitiles)
        print(f"processing: {ticker}")
        if (count%10) == 0:
            print(f"processed tickers: {count}")
        if in_value>market_cap_text:
            vaule_stock_found+=1
            print(f"Ticker: {ticker} Difference={in_value}")
            data=[[ticker,in_value]]
            with open("final_list.csv",'a',newline='') as file:
                writer=csv.writer(file)
                writer.writerow(data)
                added_to_file+=1
    except Exception:
        print(f"Eror while dealing with {ticker}")
        problem_count+=1
    count+=1
    time.sleep(2)

end_time=time.time()
total_time=end_time-start_time
print(f"total time={total_time}s")
print(f"process faild={problem_count}stocks")
print(f"total processed={count}stocks")
print(f"Total value stocks found={vaule_stock_found}")
print(f"Added to file:{added_to_file}stocks")

#data is being taken from Screener.com
#tickertape
#tijorifinance
#marketsmojo.com