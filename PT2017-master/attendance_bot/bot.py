import telegram

bot = telegram.Bot(token='284691436:AAExrkDmO8RfmfyVYE4LVTNxPixnaUW6F3U')

import json

from telegram.ext import Updater
updater = Updater(token='284691436:AAExrkDmO8RfmfyVYE4LVTNxPixnaUW6F3U')
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Ok, start! Send your student ID:")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(bot, update):
	json_data = open('students.json').read()
	students = json.loads(json_data)
	text = update.message.text
	user_id = update.message.from_user.id
	#16BD02104
	import re
	pattern = re.compile("^\d\dBD\d\d\d\d\d$")
	ok = pattern.match(text)
	if ok != None:
		kbtu_id = text
		students[user_id] = kbtu_id
		bot.sendMessage(chat_id=update.message.chat_id, text="Спасибо, Ваш student ID %s" % kbtu_id)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="Введите правильный student ID, например 16BD02104")
	with open('students.json', 'w') as outfile:
		json.dump(students, outfile)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


def here(bot, update, args):
	print(args)
	course = args[0]
	pin = args[1]

	json_data = open('students.json').read()
	students = json.loads(json_data)
	user_id = str(update.message.from_user.id)
	kbtu_id = students[user_id]
	print(kbtu_id)

	json_data = open('pins.json').read()
	print(json_data)
	pins = json.loads(json_data)
	print(pins)
	if course in pins:
		if pins[course]!= pin:
			bot.sendMessage(chat_id = update.message.chat_id, text="No, PIN %s is incorrect" % pin)
			return null 
	else:
		bot.sendMessage(chat_id = update.message.chat_id, text="No, course %s is incorrect" % course)
		return null
	
	json_data = open('attendance.json').read()
	attendance = json.loads(json_data)
	today = "09.03.2017"
	days  = attendance[course]
	ok = False
	for item in days:
		if item['date'] == today:
			item['students'].append(kbtu_id)
	print(attendance)
	with open('attendance.json', 'w') as outfile:
		json.dump(attendance, outfile)
	bot.sendMessage(chat_id = update.message.chat_id, text="No, PIN %s is incorrect" % pin)

here_handler = CommandHandler('here', here, pass_args=True)
dispatcher.add_handler(here_handler)



updater.start_polling()