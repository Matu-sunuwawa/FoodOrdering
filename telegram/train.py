
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, filters, ContextTypes, MessageHandler, Updater

from aiogram import Bot, Dispatcher, types
#Reply Keyboard
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
#Inline Keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# token: Final ='6773737938:AAEFlhrkhlpuAqrBIW0qEEadKsF8Lg__jiI'
# BOT_USERNAME = '@Train4bot'
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message):
#     await message.reply("Hello! I'm Matusala Bot, Please be in touch with me for advance.")

# button1= KeyboardButton("Hello")
# button2 = KeyboardButton("Youtube")
# keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)

# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello!!! Tanks for chatting with me! It Is My Train4!!!', reply_markup=keyboard1)

# async def kb_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text

#     if text == 'Hello':
#         await update.message.reply_text('Hi! How Are You?')
#     elif text == 'Youtube':
#         await update.message.reply_text('https://youtube.com/ALL SPIRITUALITY')
#     else:
#         await update.message.reply_text(f'Your message is {text}')

# if __name__ == '__main__':
#     print('Starting the bot....')
#     app = Application.builder().token(token).build()

#     app.add_handler(CommandHandler('start', start_command))

#     app.add_handler(CommandHandler('kb', kb_command))


#     #Polls the bot
#     print('Polling.......')
#     app.run_polling(poll_interval=3)



#---------------------GENERATING RANDOM NUMBER:

# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello!!! Tanks for chatting with me! It Is My Train4!!!\n and press /"kb1/" or /"kb2/"')


# def random_command(text: str) -> str:
#     processed: str = text.lower()

#     if 'kb1' in processed:
#         num1: str = random.randrange(1,10)
#         return num1
#     if 'kb2' in processed:
#         num2: str = random.randrange(10,100)
#         return num2
#     if 'i love python' in processed:
#         return 'Remember to subscribe'
    
#     return 'I don not understand'

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text

#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     response: str = random_command(text)

#     print('Bot:', response)
#     await update.message.reply_text(response)


# print(random.randrange(1,10))

# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f'Update {update} caused error {context.error}')

# if __name__ == '__main__':
#     print('Starting the bot....')
#     app = Application.builder().token(token).build()

#     app.add_handler(CommandHandler('start', start_command))

#     # app.add_handler(CommandHandler('kb', random_command))
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     app.add_error_handler(error)

#     #Polls the bot
#     print('Polling.......')
#     app.run_polling(poll_interval=3)


import telebot
from telebot import types

bot = telebot.TeleBot('6773737938:AAEFlhrkhlpuAqrBIW0qEEadKsF8Lg__jiI')

@bot.message_handler(commands=['quiz'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)


    num1 = types.InlineKeyboardButton('100', callback_data='answer_iron')
    num2 = types.InlineKeyboardButton('39', callback_data='answer_cotton')
    num3 = types.InlineKeyboardButton('14', callback_data='answer_same')
    no_answer = types.InlineKeyboardButton('no answer ', callback_data='no_answer')

    markup.add(num1 ,num2, num3, no_answer)

    bot.send_message(message.chat.id, '2*7 = ?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
# def answer(callback):
#     if callback.message:
#         bot.send_message(callback.message.chat.id, 'Congratulations')
def answer(callback):
    if callback.data:
        if callback.data == 'answer_same':
            bot.send_message(callback.message.chat.id, 'Congratulations')
        else:
            bot.send_message(callback.message.chat.id, 'think again!')

bot.polling()