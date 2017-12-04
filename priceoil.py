import telegram 
bot = telegram.Bot(token= '310805490:AAEQBVmxLJ3zN8CWJFIFlUPfFsbOeRFmwt4')
# updates = bot.getUpdates()
# for update in updates:
 	# users = set ()
	# print(update.message.text) 	
	# print(update.message.from_user.first_name)
	# print(update.message.from_user.id)
	# print(update.message.from_user.last_name)
	# print(users)

# def oilprice(bot, update):
# 	import requests
# 	from bs4 import BeautifulSoup 
# 	url = 'http://helios.kz/toplivo/tseny-na-benzin/'
# 	r = requests.get(url)
# 	html = r.text
# 	soup = BeautifulSoup(html, "html.parser")
# 	search= soup.select("#petroil-prices li")[0]
# 	petroil = search.select("span.name")[0].text
# 	price = search.select("span.value")[0].text
# 	wtext = petroil + " - " +   price
	
# 	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)

# 	oilprice_handler = CommandHandler('petrol',0    oilprice)
# dispatcher.add_handler(oilprice_handler)

def weather(bot, update):
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
	bot.sendMessage(chat_id =update.message.chat_id, text=wtext) 

from telegram.ext import CommandHandler
weather_handler = CommandHandler('weather', print(wtext))
dispatcher.add_handler(weather_handler)

