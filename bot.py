import telebot
from telebot import types

from config import TOKEN
from main import insert_user, is_user_exist, create_inline_markup
from location import insert_location, is_location_exist, update_location


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Зарегистрироваться', request_contact=True)
    item2 = types.KeyboardButton('Отправить геоданные', request_location=True)
    markup.add(item1, item2)

    text = 'Привет, я Бот \n Для получения данных зарегистрируйся'
    bot.send_message(message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def contact(message: types.Message):
    if message.contact is not None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Products')
        item2 = types.KeyboardButton('Cart')
        # item3 = types.KeyboardButton('Main menu')
        markup.add(item1, item2)
        if not is_user_exist(message.chat.id):
            insert_user(phone_number=message.contact.phone_number, first_name=message.contact.first_name, last_name=message.contact.last_name, chat_id=message.chat.id)

            bot.send_message(message.chat.id, 'Вы успешно зарегались', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Вы уже регались', reply_markup=markup)

@bot.message_handler(content_types=['location'])
def location(message: types.Message):
    if message.location is not None:
        if not is_location_exist(message.chat.id):
            insert_location(
                chat_id=message.chat.id,
                latitude=message.location.latitude,
                longitude=message.location.longitude
            )
            bot.send_message(message.chat.id, 'Вы успешно отправили адрес')
        else:
            update_location(
                chat_id=message.chat.id,
                latitude=message.location.latitude,
                longitude=message.location.longitude
            )
            bot.send_message(message.chat.id, 'Вы изменили геоданные')


@bot.message_handler(content_types=['text'])
def text(message: types.Message):
    if message.chat.type == 'private':
        if message.text.lower() == 'products':
            markup = create_inline_markup(
                row_width = 3,
                apple = 'Apple',
                xiaomi = 'Xiaomi',
                samsung ='Samsung'
                )


            bot.send_message(message.chat.id, 'Choose brand', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    try:
        if call.message:
            if call.data == 'apple':
                markup = create_inline_markup(
                    row_width=3,
                    iphone14 = 'Iphone 14',
                    iphone13 = 'Iphone 13',
                    iphone12 = 'Iphone 12',
                    iphone11 = 'Iphone 11',
                    iphoneX = 'Iphone X',
                    Ipad = 'Ipad',
                    goBack='<<< Back to main'
                    )
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text='Choose model:',
                    reply_markup=markup
                )
            elif call.data == 'goBack': #go_back to main menu
                markup = create_inline_markup(
                row_width = 3,
                apple = 'Apple',
                xiaomi = 'Xiaomi',
                samsung ='Samsung'
                )
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text='Choose brand:',
                    reply_markup=markup
                )
            elif call.data == 'xiaomi':
                pass
                # markup = create_inline_markup(
                #     row_width=3,
                #     redmi1 = 'Redmi 1',
                #     redmi2 = 'Redmi 2',
                    
                #     goBack='<<< Back to main'
                #     )
                # bot.edit_message_text(
                #     chat_id=call.message.chat.id,
                #     message_id=call.message.message_id,
                #     text='Choose model:',
                #     reply_markup=markup
                # )
            elif call.data =='samsung':
                pass
    except:
        pass

    

bot.polling(non_stop=True)