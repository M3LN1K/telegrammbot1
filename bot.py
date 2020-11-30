import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.Token)


@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('stikers/AnimatedSticker.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	bot.send_message(message.chat.id, "Приветик, {0.first_name}!\nЯ - {1.first_name}, и я бот для подбора машин с таких сайтов как: \navito.ru \navto.ru. \nИ так, начнем. \nВыберите марку авто. Для того, что бы посмотреть марки авто введите команду /brand"
		.format(message.from_user, bot.get_me(), parse_mode='html'))

@bot.message_handler(commands=['brand'])
def car_brand(message):
	marckup = types.InlineKeyboardMarkup(row_width=2)
	but_1 =types.InlineKeyboardButton("Buick", callback_data="Buick")
	but_2 =types.InlineKeyboardButton("Acura", callback_data="Acura")
	but_3 =types.InlineKeyboardButton("Alfa Romeo", callback_data="Alfa Romeo")
	but_4 =types.InlineKeyboardButton("Audi", callback_data="Audi")
	but_6 =types.InlineKeyboardButton("Bentley", callback_data="Bentley")
	but_7 =types.InlineKeyboardButton("Bugatti", callback_data="Bugatti")
	but_8 =types.InlineKeyboardButton("BMW", callback_data="BMW")
	but_9 =types.InlineKeyboardButton("Volvo", callback_data="Volvo")
	but_10 =types.InlineKeyboardButton("Infiniti", callback_data="Infiniti")
	but_11 =types.InlineKeyboardButton("Cadillac", callback_data="Cadillac")
	but_12 =types.InlineKeyboardButton("KIA", callback_data="KIA")
	but_13 =types.InlineKeyboardButton("Lamborghini", callback_data="Lamborghini")
	but_14 =types.InlineKeyboardButton("Land Rover", callback_data="Land Rover")
	but_15 =types.InlineKeyboardButton("Lexus", callback_data="Lexus")
	but_17 =types.InlineKeyboardButton("Mazda", callback_data="Mazda")
	but_18 =types.InlineKeyboardButton("Maserati", callback_data="Maserati")
	but_19 =types.InlineKeyboardButton("Mercedes-Benz", callback_data="Mercedes-Benz")
	but_20 =types.InlineKeyboardButton("Mini", callback_data="Mini")
	but_21 =types.InlineKeyboardButton("Mitsubishi", callback_data="Mitsubishi")
	but_22 =types.InlineKeyboardButton("Nissan", callback_data="Nissan")
	but_23 =types.InlineKeyboardButton("Peugeot", callback_data="Peugeot")
	but_24 =types.InlineKeyboardButton("Porsche", callback_data="Porsche")
	but_25 =types.InlineKeyboardButton("Renault", callback_data="Renault")
	but_28 =types.InlineKeyboardButton("Citroen", callback_data="Citroen")
	but_29 =types.InlineKeyboardButton("Subaru", callback_data="Subaru")
	but_30 =types.InlineKeyboardButton("Tesla", callback_data="Tesla")
	but_31 =types.InlineKeyboardButton("Toyota", callback_data="Toyota")
	but_32 =types.InlineKeyboardButton("Ferrari", callback_data="Ferrari")
	but_33 =types.InlineKeyboardButton("FIAT", callback_data="FIAT")
	but_34 =types.InlineKeyboardButton("Volkswagen", callback_data="Volkswagen")
	but_35 =types.InlineKeyboardButton("Ford", callback_data="Ford")
	but_36 =types.InlineKeyboardButton("Honda", callback_data="Honda")
	but_37 =types.InlineKeyboardButton("Hyundai", callback_data="Hyundai")
	but_38 =types.InlineKeyboardButton("Chevrolet", callback_data="Chevrolet")
	but_39 =types.InlineKeyboardButton("Jaguar", callback_data="Jaguar")
	
	marckup.add(but_1, but_2, but_3)
	marckup.add(but_4, but_6, but_7)
	marckup.add(but_8, but_9, but_10)
	marckup.add(but_11, but_12, but_13)
	marckup.add(but_14, but_15, but_17)
	marckup.add(but_18, but_19, but_20)
	marckup.add(but_21, but_22, but_23)
	marckup.add(but_24, but_25, but_28)
	marckup.add(but_29, but_30, but_31)
	marckup.add(but_32, but_33, but_34)
	marckup.add(but_35, but_36, but_37)
	marckup.add(but_38, but_39)

	bot.send_message(message.chat.id, "Выберите нужную вам марку.", parse_mode='html', reply_markup=marckup)

def price(message):
	marckup2 = types.InlineKeyboardMarkup(row_width=2)
	but_1 =types.InlineKeyboardButton("Buick", callback_data="Buick")
	but_2 =types.InlineKeyboardButton("Acura", callback_data="Acura")
	but_3 =types.InlineKeyboardButton("Alfa Romeo", callback_data="Alfa Romeo")
	but_4 =types.InlineKeyboardButton("Audi", callback_data="Audi")
	but_6 =types.InlineKeyboardButton("Bentley", callback_data="Bentley")
	but_7 =types.InlineKeyboardButton("Bugatti", callback_data="Bugatti")
	
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'Buick':
				sti = open('stikers/1.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Buick.")
			elif call.data == 'Acura':
				sti = open('stikers/2.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Acura.")

			elif call.data == 'Alfa Romeo':
				sti = open('stikers/3.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Alfa Romeo.")

			elif call.data == 'Audi':
				sti = open('stikers/4.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Audi.")

			elif call.data == 'Bentley':
				sti = open('stikers/6.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Bentley.")

			elif call.data == 'Bugatti':
				sti = open('stikers/7.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Bugatti.")

			elif call.data == 'BMW':
				sti = open('stikers/8.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: BMW.")

			elif call.data == 'Volvo':
				sti = open('stikers/9.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Volvo.")

			elif call.data == 'Infiniti':
				sti = open('stikers/10.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Infiniti.")

			elif call.data == 'Cadillac':
				sti = open('stikers/11.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Cadillac.")

			elif call.data == 'KIA':
				sti = open('stikers/12.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: KIA.")

			elif call.data == 'Lamborghini':
				sti = open('stikers/13.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Lamborghini.")

			elif call.data == 'Land Rover':
				sti = open('stikers/14.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Land Rover.")

			elif call.data == 'Lexus':
				sti = open('stikers/15.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Lexus.")

			elif call.data == 'Mazda':
				sti = open('stikers/17.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Mazda.")

			elif call.data == 'Maserati':
				sti = open('stikers/18.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Maserati.")

			elif call.data == 'Mercedes-Benz':
				sti = open('stikers/19.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Mercedes-Benz.")

			elif call.data == 'Mini':
				sti = open('stikers/20.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Mini.")

			elif call.data == 'Mitsubishi':
				sti = open('stikers/21.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Mitsubishi.")

			elif call.data == 'Nissan':
				sti = open('stikers/22.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Nissan.")

			elif call.data == 'Peugeot':
				sti = open('stikers/23.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Peugeot.")

			elif call.data == 'Porsche':
				sti = open('stikers/24.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Porsche.")

			elif call.data == 'Renault':
				sti = open('stikers/25.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Renault.")

			elif call.data == 'Citroen':
				sti = open('stikers/28.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Citroen.")

			elif call.data == 'Subaru':
				sti = open('stikers/29.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Subaru.")

			elif call.data == 'Tesla':
				sti = open('stikers/30.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Tesla.")

			elif call.data == 'Toyota':
				sti = open('stikers/31.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Toyota.")

			elif call.data == 'Ferrari':
				sti = open('stikers/32.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Ferrari.")

			elif call.data == 'FIAT':
				sti = open('stikers/33.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: FIAT.")

			elif call.data == 'Volkswagen':
				sti = open('stikers/34.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Volkswagen.")

			elif call.data == 'Ford':
				sti = open('stikers/35.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Ford.")

			elif call.data == 'Honda':
				sti = open('stikers/36.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Honda.")

			elif call.data == 'Hyundai':
				sti = open('stikers/37.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Hyundai.")

			elif call.data == 'Chevrolet':
				sti = open('stikers/38.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Chevrolet.")

			elif call.data == 'Jaguar':
				sti = open('stikers/39.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

				marckup1 = types.InlineKeyboardMarkup(row_width=2)
				but_1 =types.InlineKeyboardButton("Назад", callback_data="Back")
				but_2 =types.InlineKeyboardButton("Продолжить", callback_data="Continue")

				marckup1.add(but_1, but_2)

				bot.send_message(call.message.chat.id, 'Мы можем продолжить?', reply_markup=marckup1)
				# remove inline buttons
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш выбор: Jaguar.")

			elif call.data == 'Back':
			# show alert
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="Вы вернулись к выбору марок!")
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ВЫ вернулись к выбору марки.", reply_markup=car_brand(call.message))

			elif call.data == 'Continue':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ВЫберите цену аватомобиля в диапозонах: ", reply_markup=(call.message))



			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="Вы выбрали марку!")

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)