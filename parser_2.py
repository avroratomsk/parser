from selenium import webdriver
from bs4 import BeautifulSoup
import time

page = 1

page_limit = 5

list_proxy = []
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

# Сайты с объединенный ip и port
urls = [
    f"http://free-proxy.cz/en/proxylist/country/RU/all/ping/all/{page}",
    f"https://www.proxydocker.com/ru/proxylist/country/Russia",
    f"https://proxy-tools.com/proxy/ru?page={page}",
]


driver = webdriver.Firefox()
driver.get("https://www.proxydocker.com/ru/proxylist/country/Russia")

# Wait for the JavaScript to load
time.sleep(5)

# Get the page source
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract the data
table = soup.find("table")

# table = soup.find(
#     "table", attrs={"class": "table table-sm table-responsive-md table-hover"}
# )

data = []
table_body = table.find("tbody")
# driver.find_element_by_class_name("badge badge-primary").click()
for row in table_body.find_all("tr"):
    data.append([cell.text for cell in row.find_all("td")])

# Close the browser
driver.quit()

print(data)
