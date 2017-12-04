import requests 
token = "5422355d35941a74a970f9bb80441debc01d8dae8901213ccd8de058338e9aa65f14f635f92fce39e64fe"

url = "http://www.vktops.com/statusy-pro-druzey/"

r = requests.get(url)
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
status_list = soup.select(".statusesList .statusesList-item div.text")
statuses = []
for item in status_list:
	statuses.append(item.text)
import random 
p = random.randrange( len(statuses))
text = statuses[p]             
print(text)
url = 'https://api.vk.com/method/status.set?text=%s&v=5.52&access_token=%s' %(text, token)
r = requests.get(url)
print(r.text)
