import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
page = 1

page_limit = 5

list_proxy = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

url = f"https://www.freeproxy.world/?type=&anonymity=&country=RU&speed=&port=&page={page}"
url_two = f"https://proxyhub.me/en/ru-http-proxy-list.html"
url_three = f"https://freeproxylist.cc/online/Russia/"
url_four = f"https://proxy-tools.com/proxy/ru?page={page}"
url_five = f"https://freeproxyupdate.com/russia-ru"
url_six = f"http://free-proxy.cz/en/proxylist/country/RU/all/ping/all/{page}"

def get_proxy(url,ip,port,type,page):
    while page <= page_limit:
        URL_TEMPLATE = url
        r = requests.get(URL_TEMPLATE, headers=headers)
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
                    list_proxy.append([elem[ip],elem[port],elem[type]])
        else: 
            print(r.status_code)
        page += 1
    print(list_proxy)

get_proxy(url,0,1,5,page)
get_proxy(url_two,0,1,2,page)
get_proxy(url_three,0,1,5,page)
# get_proxy(url_four,0,1,2,page)
get_proxy(url_five,0,1,3,page)
# print(len(list_proxy))
    








# list_best_proxies = []
# URL_BEST_PROXIES = "https://api.best-proxies.ru/proxylist.txt?key=7cca8d3696dfcfb9b11082f074cc4af1&limit=0&type=http,https,socks4,socks5&country=ru"
# r = requests.get(URL_BEST_PROXIES)
# if r.status_code == 200:
#     data = r.text
#     list_best_proxies.append(data)
    
#     print(list_best_proxies)


