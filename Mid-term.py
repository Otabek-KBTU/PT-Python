import requests 
from bs4 import BeautifulSoup

url = "http://www.accuweather.com/ru/kz/astana/222343/daily-weather-forecast/222343"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
search = soup.select("#content")
looking = search.select("div span")[0].text
weather = looking.select("li span.name")[0] 
print(weather + " - ")
