import telebot
import random
from telebot import types


rank_sz = 13
suit_sz = 4

bot = telebot.TeleBot('1777554653:AAEpQNGykxEo7KdoZmEVDCj5nFFSvZwm8AM')

button1 = types.KeyboardButton("Начать игру")

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add(button1)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет", reply_markup=keyboard1)
    bot.register_next_step_handler(message, start)

def start(message):
	
	bot.send_message(message.chat.id, "Убираем клавиатуру", reply_markup=types.ReplyKeyboardRemove())

	all_cards = {("2", "♠"): 2, ("2", "♥"): 2, ("2", "♦"): 2, ("2", "♣"): 2, ("3", "♠"): 3, ("3", "♥"): 3, ("3", "♦"): 3, ("3", "♣"): 3,
	("4", "♠"): 4, ("4", "♥"): 4, ("4", "♦"): 4, ("4", "♣"): 4, ("5", "♠"): 5, ("5", "♥"): 5, ("5", "♦"): 5, ("5", "♣"): 5,
	("6", "♠"): 6, ("6", "♥"): 6, ("6", "♦"): 6, ("6", "♣"): 6, ("7", "♠"): 7, ("7", "♥"): 7, ("7", "♦"): 7, ("7", "♣"): 7,
	("8", "♠"): 8, ("8", "♥"): 8, ("8", "♦"): 8, ("8", "♣"): 8, ("9", "♠"): 9, ("9", "♥"): 9, ("9", "♦"): 9, ("9", "♣"): 9,
	("10", "♠"): 10, ("10", "♥"): 10, ("10", "♦"): 10, ("10", "♣"): 10, ("J", "♠"): 10, ("J", "♥"): 10, ("J", "♦"): 10, ("J", "♣"): 10,
	("Q", "♠"): 10, ("Q", "♥"): 10, ("Q", "♦"): 10, ("Q", "♣"): 10, ("K", "♠"): 10, ("K", "♥"): 10, ("K", "♦"): 10, ("K", "♣"): 10,
	("A", "♠"): 11, ("A", "♥"): 11, ("A", "♦"): 11, ("A", "♣"): 11}

	#global s
	s = 0
	old_str = "\0"

	#while s <= 21:

	my_cards = random.choice(list(all_cards.keys()))

	index = all_cards[my_cards]

	s += index

	all_cards.pop(my_cards)

	def new_mes(message):

			nonlocal flag
			nonlocal s
			nonlocal all_cards
			nonlocal my_cards

			if message.text.lower() == 'еще':
				my_cards = random.choice(list(all_cards.keys()))

				index = all_cards[my_cards]

				s += index

				all_cards.pop(my_cards)

			#elif message.text.lower() == 'стоп':

			#elif message.text.lower() == 'сплит':

			#elif message.text.lower() == 'дабл':
			flag = 1

	#keyboard3 = telebot.types.ReplyKeyboardMarkup()
	button3 = types.KeyboardButton("Еще")
	button4 = types.KeyboardButton("Стоп")
	button5 = types.KeyboardButton("Сплит")
	button6 = types.KeyboardButton("Дабл")
	#keyboard3.add(button3).add(button4).add(button5).add(button6)

	while s > -1:
		keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		button2 = types.KeyboardButton(old_str + my_cards[0] + my_cards[1] + '\n' + 'Сумма = ' + str(s))
		keyboard2.add(button2).add(button3).add(button4).add(button5).add(button6)

		if s > 21 :
			bot.send_message(message.chat.id, "Перебор!", reply_markup=keyboard2)
			break

		old_str += my_cards[0] + my_cards[1]

		bot.send_message(message.chat.id, "Ваши карты", reply_markup=keyboard2)
		bot.register_next_step_handler(message, new_mes)
		flag = 0
		while flag == 0:
			1

	keyboard4 = telebot.types.ReplyKeyboardMarkup()
	keyboard4.add(old_str + my_cards[0] + my_cards[1] + '\n' + 'Сумма = ' + str(s)).add("Начать заново").add("Конец")
	bot.send_message(message.chat.id, "Еще раз?", reply_markup=keyboard4)
	bot.register_next_step_handler(message, end_func)


def end_func(message):
	if message.text.lower() == 'начать заново':
		bot.send_message(message.chat.id, "Хорошо")
		start(message)
	elif message.text.lower() == 'конец':
		bot.send_message(message.chat.id, "До свидания")

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
