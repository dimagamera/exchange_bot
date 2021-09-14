import telebot
from telebot.types import Message
from database.bd import *
from lib.api import token
from lib.history import *
from lib.lst import *

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])

def send_welcome(message):
	if message.text == '/start':
		bot.send_message(message.chat.id, '*Что умеет данный бот?*\n\n */lst* - _показывать курс валют (CAD, RUS, UAH)_\n*/exchange* - _конвертировать валюту_(/exchange 100 UAH) -> (100$ в UAH)\n*/history* - _курс валюты за последние 7 дней_ (/history CAD)\n*Доступные валюты*: _UAH, RUS, CAD_\n*Базовая валюта*: USD', parse_mode="Markdown")
	
	elif message.text == '/lst':
		res = time()
		if res >= 10:
			update()
			into()
			rows = show()
			for item in rows:
				bot.send_message(message.chat.id, '*Валюта*: ' +str(item[0])+'\n*Курс*: '+str(item[1]),  parse_mode="Markdown")
		else:
			rows = show()
			for item in rows:
				bot.send_message(message.chat.id, '*Валюта*: ' +str(item[0])+'\n*Курс*: '+str(item[1]),  parse_mode="Markdown")

	elif message.text[:9] == '/exchange':
		currency = message.text[-3:]
		dollars = message.text.replace('/exchange ', '').replace('USD', '').replace('$', '').split(' ')[0]
		curr = find(currency)
		try:
			for item in curr:
				res = float(dollars)*float(item[1])
			bot.send_message(message.chat.id,str(res))
		except:
			bot.send_message(message.chat.id, '*Currency not found*')

	elif message.text[:8] == '/history':
		history = message.text.replace('/history ', '')
		if graffi(history)!='error': 
			photo = open('lib/history.png', 'rb')
			bot.send_photo(message.chat.id, photo)
		else:
			bot.send_message(message.chat.id, 'Currency not found')

bot.polling(none_stop=True)
