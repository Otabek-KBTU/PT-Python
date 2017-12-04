import telegram 
bot = telegram.Bot(token= '310805490:AAEQBVmxLJ3zN8CWJFIFlUPfFsbOeRFmwt4')
from telegram.ext import Updater
updater = Updater(token='310805490:AAEQBVmxLJ3zN8CWJFIFlUPfFsbOeRFmwt4')
dispatcher = updater.dispatcher
def weather(bot, update):
	
	# print(update.message.text)B
	import requests 
	from bs4 import BeautifulSoup
	url = "http://www.accuweather.com/ru/kz/astana/222343/weather-forecast/222343"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	rows = soup.select("#content")
	for tr in rows:
		name = tr.select("span.large-temp")[0].text
	# rate = float(tr.select("td span.today")[0].text.replace(",", "."))
	print(name+ " : " "Astana")
	print("Now, outside is cold. Take with you a coat and hat!")
	wtext = print
	bot.sendMessage(chat =update.message.chat_id, text=wtext) 

from telegram.ext import CommandHandler
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)
