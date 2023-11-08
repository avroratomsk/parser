import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = 1

page_limit = 5

list_proxy = []
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

urls = [
    # f"https://www.freeproxy.world/?type=&anonymity=&country=RU&speed=&port=&page={page}",  # Работает
    # f"https://proxyhub.me/en/ru-http-proxy-list.html",  # Работает
    # f"https://freeproxylist.cc/online/Russia/",  # Работает
    # f"https://proxy-tools.com/proxy/ru?page={page}", # - Ajax
    # f"https://freeproxyupdate.com/russia-ru",  # Работает
    # f"http://free-proxy.cz/en/proxylist/country/RU/all/ping/all/",
    # f"https://hidemy.io/ru/proxy-list/countries/russian-federation/",  # Работает
]


def get_proxy(url, mass):
    # ip = [mass[0]]
    # port = [mass[1]]
    # protocol = [mass[2]]
    print(mass)

    URL_TEMPLATE = url
    r = requests.get(URL_TEMPLATE, headers=headers)
    try:
        soup = bs(r.text, "html.parser")
        table_body = soup.find("table")
        rows = table_body.find("tbody")
        rows_tr = rows.find_all("tr")
        data = []
        for row in rows_tr:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        for elem in data:
            ip = mass[0]
            port = mass[1]
            if len(elem) > 0:
                list_proxy.append([elem[ip], elem[port]])
    except Exception as e:
        print(e, "Error")


def proxy(urls):
    print(len(urls))
    for site in urls:
        response = requests.get(site, headers=headers)
        soup = bs(response.text, "html.parser")
        table_body = soup.find("table")
        table_head = table_body.find("thead")

        if table_head == None:
            table_body = soup.find("table", {"id": "proxy_list"})
            table_head = table_body.find("thead")

        table_head_tr = table_head.find("tr")
        table_head_th = table_head_tr.find_all("th")
        if table_head_th == []:
            table_head_th = table_head_tr.find_all("td")

        i = 0
        ip = 0
        port = 0
        protocol = 0
        mass_config = []
        for th in table_head_th:
            if (
                th.text.strip() == "IP adress"
                or th.text.strip() == "IP Address"
                or th.text.strip() == "IP address"
                or th.text.strip() == "IP"
                or th.text.strip() == "IP адрес"
                or th.text.strip() == "IP : порт"
            ):
                ip = i
                mass_config.append(ip)
            if th.text.strip() == "Port" or th.text.strip() == "Порт":
                port = i
                mass_config.append(port)

            if (
                th.text.strip() == "Type"
                or th.text.strip() == "Protocol"
                or th.text.strip() == "Тип"
            ):
                protocol = i
                mass_config.append(protocol)

            i += 1
        get_proxy(site, mass_config)


proxy(urls)
print(list_proxy)
print(len(list_proxy))

# urls_api = [f"https://advanced.name/freeproxy/6540c68128b1c?country=RU"]
# connect_url = requests.get("https://spys.one/free-proxy-list/RU/")
# soup_2 = bs(connect_url.text, "html.parser")
# print(soup_2)

# list_best_proxies = []
# URL_BEST_PROXIES = "https://api.best-proxies.ru/proxylist.txt?key=7cca8d3696dfcfb9b11082f074cc4af1&limit=0&type=http,https,socks4,socks5&country=ru"
# r = requests.get(URL_BEST_PROXIES)
# if r.status_code == 200:
#     data = r.text
#     list_best_proxies.append(data)

#     print(list_best_proxies)
