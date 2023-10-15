import pandas
import tools
import time
from bs4 import BeautifulSoup

start_timer = time.time()
Security_Code_list =tools.stock_security_list() 
count = 0
filed_count=0
final_list = []

for security_code in Security_Code_list:
    print(security_code)
    if count == 100000:
        break
    security_code = str(security_code)
    try:
        data = pandas.read_html("/home/yashas/Desktop/Stocks/DATA/" + security_code + ".html")
        PandL = data[1].copy().transpose()
        sales = PandL[0].copy().tolist()
        OPMp = PandL[3].copy().tolist()

        sales = sales[-5:]
        OPMp = OPMp[-5:]
        
        sales_flag=tools.sales_check(sales)

        OPMp_flag=tools.OPMp_check(OPMp)

        # To check if P/E condition is met
        with open("/home/yashas/Desktop/Stocks/DATA/" + security_code + ".html", "r") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        numbers = soup.findAll('li', class_="flex flex-space-between")
        for number in numbers:
            if "Stock P/E" in number.text:
                stock_PtoE = number.find('span', class_='number').text
        PtoE_flag=tools.Stock_PtoE_check(stock_PtoE)

        if PtoE_flag == 1 and sales_flag == 1 and OPMp_flag == 1:
            final_list.append(security_code)
            print(final_list)
    except Exception as e:
        print(f"failed to prcocess: {security_code}")
        print(str(e))
        filed_count+=1
    count += 1

end_timer = time.time()

print("Total time taken =", end_timer - start_timer)
print("Failed to scan:",filed_count)
print("Final List:", final_list)
