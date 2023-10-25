import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
page = 1

page_limit = 2

list_proxy = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

while page <= page_limit:
    URL_TEMPLATE = f"https://www.freeproxy.world/?type=&anonymity=&country=RU&speed=&port=&page={page}"
    r = requests.get(URL_TEMPLATE, headers=headers)
    # print(r)
    if r.status_code == 200:
        soup = bs(r.text, "html.parser")
        table_body = soup.find('table')
        rows = table_body.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])


        for elem in data:
            if(len(elem) > 0):
                list_proxy.append([elem[0],elem[1],elem[5]])
    else: 
        print(r.status_code)

    page += 1
            

print(list_proxy)
