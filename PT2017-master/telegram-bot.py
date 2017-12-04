import telegram
bot = telegram.Bot(token='284691436:AAExrkDmO8RfmfyVYE4LVTNxPixnaUW6F3U')
# updates = bot.getUpdates()
# users = set()
# for update in updates:
# 	print(update.message.text)
# 	print(update.message.from_user.id)
# 	print(update.message.from_user.first_name)
# 	print(update.message.from_user.last_name)
# 	users.add(update.message.from_user.id)
# print(users)
# users = [301297584, 129767043, 242964805, 279884361, 149403787, 211076013, 239499600, 376072028]
# for user_id in users:
# 	bot.sendMessage(chat_id = user_id, text = 'Sorry')

from telegram.ext import Updater
updater = Updater(token='284691436:AAExrkDmO8RfmfyVYE4LVTNxPixnaUW6F3U')
dispatcher = updater.dispatcher

def say_start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Ok, start!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', say_start)
dispatcher.add_handler(start_handler)

def say_salem(bot, update):
	name = update.message.from_user.first_name
	bot.sendMessage(chat_id = update.message.chat_id, text = 'Salem, %s' % name)

from telegram.ext import CommandHandler
salem_handler = CommandHandler('salem', say_salem)
dispatcher.add_handler(salem_handler)

def weather(bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://kazhydromet.kz/ru/almaty'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)

weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)


def echo(bot, update):
	if "привет" in update.message.text.lower():
		wtext = 'Салам пополам'	
	else:
		wtext = "Че там, %s" % update.message.from_user.first_name
	bot.sendMessage(chat_id=update.message.chat_id, text=wtext)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()





