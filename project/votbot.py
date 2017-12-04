import telegram

bot = telegram.Bot(token='310805490:AAEQBVmxLJ3zN8CWJFIFlUPfFsbOeRFmwt4')

import json

from telegram.ext import Updater
updater = Updater(token='310805490:AAEQBVmxLJ3zN8CWJFIFlUPfFsbOeRFmwt4')
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Hello, let's start! First write your specialty (/ask) and send your student ID:(/echo)")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def ask(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Who are you? Student or teacher?")
	
	json_data = open('whoisit.json').read()
	whoisit = json.loads(json_data)
	text = update.message.text
	user_id = update.message.from_user.id
	import re
	pattern = re.compile("^\dTeacher")
	ok = pattern.match(text)
	if ok != None:
		idfy_id = text
		
		whoisit[user_id] = idfy_id
		bot.sendMessage(chat_id=update.message.chat_id, text="I am glad to see you Teacher ")
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="Ok, student continue working...")
	with open('whoisit.json', 'w') as outfile:
		json.dump(whoisit, outfile)

from telegram.ext import CommandHandler
ask_handler = CommandHandler('ask', ask)
dispatcher.add_handler(ask_handler)



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
		bot.sendMessage(chat_id=update.message.chat_id, text="Thanks. Dear student, your student ID accepted and  your student ID is %s" % kbtu_id)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="Your stydent ID is incorrect. Send your student ID, for example: 16BD02104")
	with open('students.json', 'w') as outfile:
		json.dump(students, outfile)

	import re
	pattern = re.compile("^\d\dFX\d\d\d\d\d$")
	ok = pattern.match(text)
	if ok != None:
		
		kbtu_id = text
		students[user_id] = kbtu_id
		bot.sendMessage(chat_id=update.message.chat_id, text="Thanks. Dear Teacher, your ID accepted and  your student ID is %s" % kbtu_id)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="If you are a Teacher your ID is incorrect. Send your ID, for example: 16FX07077")

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def course(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Dear student, send the pins of the course!")
	
	
-

def here(bot, update, args):
	print(args)
	course = args[0]
	pin = args[1]
	# import re
	# pattern = re.compile("^\d\d\d\d$")
	# ok = pattern.match(text)
	# if ok != None:
	json_data = open('students.json').read()
	students = json.loads(json_data)
	user_id = str(update.message.from_user.id)
	kbtu_id = students[user_id]
	print(kbtu_id)
	bot.sendMessage(chat_id = update.message.chat_id, text="No, PIN %s is incorrect" % pin)
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
	today = "26.04.2017"
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