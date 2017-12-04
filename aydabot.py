import time
import telegram
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler 
import requests 

def get_last(uid1):
	uid = str(uid1) 
	url = 'https://api.vk.com/method/users.get?user_ids=%s&fields=status,last_seen,blacklisted,home_town&name_case=dat' 
	r = requests.get(url % uid) 
	data = r.json()
	print(data)
	last_seen = data['response'][0]['last_seen']['time']
	platform = data['response'][0]['last_seen']['platform']  

	print(last_seen)
	print (last int(time.mktime(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))))

	return last_seen, platform



  
bot = telegram.Bot(token='355638441:AAFfaqQCceiTQvRPokoAGs18F2l4Ufgx5wo')


updater = Updater(token='355638441:AAFfaqQCceiTQvRPokoAGs18F2l4Ufgx5wo')
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Hello what's your uid")
	hab()

def hab(bot, update):
	idwka = update.message.text
	print(idwka)
	last_seen, platform = get_last(idwka)
	bot.sendMessage(chat_id = update.message.chat_id, text = 'last seen: {}\nplatform: {}'.format(last_seen,platform))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

id_handler = MessageHandler(Filters.text, hab)
dispatcher.add_handler(id_handler)
updater.start_polling()