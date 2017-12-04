
# import requests 
# from bs4 import BeautifulSoup

# url = "https://mig.kz/"
# r = requests.get(url)
# html = r.text
# soup = BeautifulSoup(html, "html.parser")
# row = soup.select("div.informer table tr")[0]
# name = row.select("td.currency")[0].text
# rate = row.select("td.sell")[0].text
# print(name + " " + rate) 
import requests 
from bs4 import BeautifulSoup

url = "https://mig.kz/"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("div.col-xs-12 table h1")[0]
name = row.select("li.span.name")[0].text
rate = row.select("li.span.value")[0].text
print(name + " " + rate)
