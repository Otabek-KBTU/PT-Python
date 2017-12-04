import requests 
import io
from bs4 import BeautifulSoup
url= "https://m.tengrinews.kz/ru/ajax/GetLatestNews?page=%d"
with open("output.txt", "wb") as file:
	for page in range(1, 2):
		r = requests.get(url % page)
		soup = BeautifulSoup(t.text, "html.parser")
		links = soup.select("a")
		for link in links
		file.write(r.text.encode('utf-8'))
		file.write("\n".encode('utf-8'))
#https://tengrinews.kz/ajax/getLatestNews?page=%d
