import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # we add r to pass a row string
redirect="127.0.0.1"
website_list=["www.bewiv.com","bewiv.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
       print("working time...")
       with open(hosts_temp, 'r+') as file:
           content=file.read()
           for website in website_list:
               if website in content:
                   pass
               else:
                   file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0) # to put all the text in the begin
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("fun hours...")
    time.sleep(5)
