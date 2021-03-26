import socket
import time
from selenium import webdriver
chromedriver="chromedriver.exe"

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
list_ip=["192.168.204.2","192.168.204.3"]
#checking valid ip address
for i in list_ip:
    if i==ip_address:
        print("valid ip Address-checked")
        print("YOUR IP:"+ip_address)
        break
    else:
        print("NOT A VALID IP ADDRESS, SOFTWARE WILL AUTMATICALLY CLOSE IN 5 SECONDS")
        time.sleep(5)
        quit()
time.sleep(3)
Dict ={"192.168.204.2":"DESKTOP-U0D8I03", "192.168.204.3":"Aniket" }
#checking either IP address get's matched with it's host name or not
if Dict[ip_address]==hostname:
        print("Host name got matched with your Ip address")
else:
        print("Not a valid host name,SOFTWARE WILL AUTOMATICALLY CLOSE IN 5 SECONDS")
        quit()
print("**********************************************************************************************************************")
print("Please Enter Govt. License")        
govt_license=input()
govt_dict={"DESKTOP-U0D8I03":"GOVT123456", "DESKTOP-U0D8I04":"GOVT123457"}
#checking hostname getting matched with the govt license or not
if govt_dict[hostname]==govt_license:
    print("correct")
else:
    print("Entered wrong password,software will automatically close in 5 seconds")
    time.sleep(5)
    quit()
#opening website or we can open any database,software etc.
driver=webdriver.Chrome(chromedriver)
driver.get("file:///C:/Users/lenovo/Desktop/duo/index.html")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
#open browser through selenium
