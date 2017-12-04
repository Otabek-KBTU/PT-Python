import telegram
bot = telegram.Bot(token='310805490:AAEQBVmxLJ3zN8CWJFIFlUPfFsbOeRFmwt4')

from telegram.ext import Updater
updater = Updater(token='310805490:AAEQBVmxLJ3zN8CWJFIFlUPfFsbOeRFmwt4')
dispatcher = updater.dispatcher
import json
parsed_json = json.loads(chat_id)
data = json.dumps(chat_id)
def say_start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Ok, start!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', say_start)
dispatcher.add_handler(start_handler)

def chat_id(bot, update):
	name = update.message.from_user.first_name
	bot.sendMessage(chat_id = update.message.chat_id, text = 'Your chat id:, %s' % name)

from telegram.ext import CommandHandler
id_handler = CommandHandler('your_id', chat_id)
dispatcher.add_handler(id_handler)


def student_id(bot, update):
	p = re.compile('^\d\d/\d\d/\d\d\d\d$')
	print(p.match(''))  
	if p in update.message.text.lower():
		wtext = "Your id accepted"	
	else:
		wtext = "Yor student id not accepted, %s" % update.message.from_user.first_name
	bot.sendMessage(chat_id=update.message.chat_id, text='Student id:, %s' % name )

from telegram.ext import MessageHandler, Filters
student_id_handler = MessageHandler(Filters.text, student_id)
dispatcher.add_handler(student_id_handler)


updater.start_polling()
