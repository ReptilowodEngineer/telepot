import time, datetime  # Importing the datetime library
import telepot  # Importing the telepot library
from telepot.loop import MessageLoop  # Library function to communicate with telegram bot

from time import sleep  # Importing the time library to provide the delays in program,.
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


nas_p=""

def pogoda(chat_id, nas_p):
	bot.sendMessage(chat_id, ("Погода в"+nas_p))
def smena_n_p(chat_id, msg):
	bot.sendMessage(chat_id, "Напишите название населенного пункта на английском")
	nas_p=msg['text']
	return nas_p
# Getting date and time
def fact(chat_id):
	fac=""
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    if command == '/start':
        markup = ReplyKeyboardMarkup(keyboard=[
            [dict(text='Погода')],
            [dict(text='Смена населенного пункта')],
            [dict(text='Интересный факт')],])


        bot.sendMessage(chat_id, "Привет. Я многофункциональный метеобот. Укажите название вашего населенного пункта на английском.", reply_markup=markup) 
    elif command == 'Погода':
    	global nas_p
    	pogoda(chat_id, nas_p)
    elif command == 'Смена населенного пункта':
    	smena_n_p(chat_id, msg)
    elif command == 'Интересный факт':
    	fact(chat_id)
    else:
    	nas_p=command





# elif command == '/logo':
# telegram_bot.sendPhoto (chat_id, photo="https://i.pinimg.com/avatars/circuitdigest_1464122100_280.jpg")

# Insert your telegram token below
bot = telepot.Bot('1754213635:AAEop3dnHd1tQPcFuMsxL6EywTc6fJUUasY')
print(bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, action).run_as_thread()
print('Listening....')

while 1:
    sleep(1)
