#Stocks

1.Run download_data.py to download data from https://www.screener.in. Alter path as needed
2.Run Bro'sScan.py to obtain equities that meet the following conditions:
    Sales growth >= 12% (Last 5 years)
    Operating Profit Margin (OPM%) >= 10% (Last 5 years)
    Price-to-Earnings Ratio (P/E) <= 10
3.Equity.csv contains the list of equities on BSE, which can be found at https://www.bseindia.com/corporates/List_Scrips.html.
4.It takes approximately 2 hours to run download_data.py and around 10 minutes to run Bro'sScan.py.
5.net_net.py does not provide any equity as the market is too efficient for it to work effectively.
6.report_generator.py generates a simple report for any stock by taking security code as input.
7.tools.py and report_tools.py contains functions used by Bro'sScan and report_generator.py.
8.Stock_auto.py was the first scan written in this project, and it is an earlier version of net_net.py. It also does not work for the same reason.
9.Other files here are currently under development
