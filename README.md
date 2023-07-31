Stocks
1.Run download_data.py to download data from https://www.screener.in. Alter path as needed\n
2.Run Bro'sScan.py to obtain equities that meet the following conditions:\n
    Sales growth >= 12% (Last 5 years)\n
    Operating Profit Margin (OPM%) >= 10% (Last 5 years)\n
    Price-to-Earnings Ratio (P/E) <= 10\n
3.Equity.csv contains the list of equities on BSE, which can be found at https://www.bseindia.com/corporates/List_Scrips.html.\n
4.It takes approximately 2 hours to run download_data.py and around 10 minutes to run Bro'sScan.py.\n
5.net_net.py does not provide any equity as the market is too efficient for it to work effectively.\n
6.Stock_auto.py was the first scan written in this project, and it is an earlier version of net_net.py. It also does not work for the same reason.\n
7.Other files here are currently under development\n