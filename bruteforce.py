import requests
from concurrent.futures import ThreadPoolExecutor
import requests
import colorama
import time
from colorama import Fore
class colors:
    black = Fore.LIGHTBLACK_EX
    blue = Fore.LIGHTBLUE_EX
    cyan = Fore.LIGHTCYAN_EX
    green = Fore.LIGHTGREEN_EX
    magenta = Fore.LIGHTMAGENTA_EX
    red = Fore.LIGHTRED_EX
    white = Fore.LIGHTWHITE_EX
    yellow = Fore.LIGHTYELLOW_EX
c = colors()
banner = c.cyan + """

  _____      _                  _____ _     _      _     _ 
 / ____|    | |                / ____| |   (_)    | |   | |
| |    _   _| |__   ___ _ __  | (___ | |__  _  ___| | __| |
| |   | | | | '_ \ / _ \ '__|  \___ \| '_ \| |/ _ \ |/ _` |
| |___| |_| | |_) |  __/ |     ____) | | | | |  __/ | (_| |
 \_____\__, |_.__/ \___|_|    |_____/|_| |_|_|\___|_|\__,_|
        __/ |                                              
       |___/                                                                                                                        

                        { v1.0.1 }

      Omer Simko, Zhyar Muhamad ,Safin Mohammed Othman , Ahmad A Abdulla

please 'bruteforce.py URL'
"""

print(banner)

# worker thread to process one url:

def proccess_url(url, session):
    r = session.get(url)
    print(url)
    if r.status_code == 200:
        print('this page' + url + ' is avable')
        with open('/root/Desktop/23/2.txt', 'a') as f:
            
            f.write('\n')
            f.write(url)
            f.write('\n')


url = input("Host [http://site.com] >>> " )
#create all the urls:
with open('/root/Desktop/23/1.txt','r') as redfile:
    urls = [url + '/' + x.rstrip() for x in redfile]

with ThreadPoolExecutor(max_workers=1) as executor:
    session = requests.Session()
    futures = [executor.submit(proccess_url, url, session) for url in urls]
    for future in futures:
        future.result()
proccess_url()        
