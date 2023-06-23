import pandas
import time
from bs4 import BeautifulSoup

start_timer = time.time()
stock_list = pandas.read_csv("/home/yashas/Desktop/Quant/NET_NET/Equity.csv")
Security_Code_list = stock_list.index.to_list()
count = 0
filed_count=0
final_list = []

for security_code in Security_Code_list:
    print(security_code)
    if count == 10000:
        break
    security_code = str(security_code)
    try:
        data = pandas.read_html("/home/yashas/Desktop/Quant/DATA/" + security_code + "/" + security_code + ".html")
        PandL = data[1].copy().transpose()
        sales = PandL[0].copy().tolist()
        OPMp = PandL[3].copy().tolist()

        sales = sales[-5:]
        OPMp = OPMp[-5:]
        

        # To check if sales condition is met
        sales_flag = 1
        for i in range(len(sales) - 1):
            sales[i]=str(sales[i])
            if "," in sales[i]:
                sales[i]=sales[i].replace(",","")
                
            if float(sales[i]) == 0:
                #print(sales[i])
                continue
            else:
                if ((float(sales[i + 1]) - float(sales[i])) / float(sales[i])) * 100 < 12:
                    sales_flag = 0
                    break

        # To check if OPM% condition is met
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

        # To check if P/E condition is met
        with open("/home/yashas/Desktop/Quant/DATA/" + security_code + "/" + security_code + ".html", "r") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        numbers = soup.findAll('li', class_="flex flex-space-between")
        for number in numbers:
            if "Stock P/E" in number.text:
                stock_PtoE = number.find('span', class_='number').text
        if "," in stock_PtoE:
            stock_PtoE=stock_PtoE.replace(",","")
        PtoE_flag = 0
        if stock_PtoE=="":
            PtoE_flag=0
        else:
            if float(stock_PtoE) <= 20:
                PtoE_flag = 1
        if PtoE_flag == 1 and sales_flag == 1 and OPMp_flag == 1:
            final_list.append(security_code)
            print(final_list)
    except Exception:
        print(f"failed to prcocess: {security_code}")
        filed_count+=1
    count += 1

end_timer = time.time()

print("Total time taken =", end_timer - start_timer)
print("Failed to scan:",filed_count)
print("Final List:", final_list)
