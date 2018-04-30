import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # we add r to pass a row string
redirect="127.0.0.1"
website_list=["www.hespress.com","hespress.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
       print("working time...")
       time.sleep(5)
