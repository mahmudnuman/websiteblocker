import time as t
from datetime import datetime as dt


host_temp="hosts"
hosts_paths=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=[
    "www.facebook.com",
    "facebook.com",
    "www.yahoo.com",
    "yahoo.com"
    ]
number=0
while True:
    time = dt.now()

    current_hour=time.hour
    #current_hour=9
    if ((8<=current_hour<=17)):
       # print('Working Hours')
        with open(hosts_paths,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write( redirect + " " + website + "\n")
                    
                
    else:
        with open(hosts_paths,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
       # print('Fun Hours')

    t.sleep(5)
    