import telebot
import time
from telebot import types

day = 0
mes = ''

wdays = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

button1 = types.KeyboardButton(wdays[0])
button2 = types.KeyboardButton(wdays[1])
button3 = types.KeyboardButton(wdays[2])
button4 = types.KeyboardButton(wdays[3])
button5 = types.KeyboardButton(wdays[4])
button6 = types.KeyboardButton(wdays[5])
button7 = types.KeyboardButton(wdays[6])

bot = telebot.TeleBot('1555929789:AAFVd9jWyyPWMEOz2NKqguNZmE3IHowSydQ')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.add(button1).add(button2).add(button3).add(button4).add(button5).add(
	button6).add(button7)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите, в какой день вам прислать сообщение', 
    	reply_markup=keyboard1)
    bot.register_next_step_handler(message, get_day)

def get_day(message):
	global day 
	day = wdays.index(message.text)

	bot.send_message(message.chat.id, 'Какое сообщение вам отправить?', reply_markup=types.ReplyKeyboardRemove())
	bot.register_next_step_handler(message, get_message)

def get_message(message):
	global mes

	mes = message.text

	bot.send_message(message.chat.id, 'Введите нужное время в формате hh:mm')
	bot.register_next_step_handler(message, get_hours)

def get_hours(message):
	global day
	local_day = day

	bot.send_message(message.chat.id, 'Будет сделано!')

	hour = int(message.text[0:2])
	mins = int(message.text[3:5])

	global mes
	local_mes = mes.expandtabs(1)

	while True:
		now_tm = time.localtime(time.time())

		if(now_tm[3] == hour and now_tm[4] == mins and now_tm[6] == local_day and now_tm[5] == 0):
			bot.send_message(message.chat.id, local_mes)
			time.sleep(5)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, interval=0)
