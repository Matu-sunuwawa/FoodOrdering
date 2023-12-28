
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, filters, ContextTypes, MessageHandler,Updater, CallbackQueryHandler, CallbackContext
import telebot
from telebot import types

bot = telebot.TeleBot('6773737938:AAEFlhrkhlpuAqrBIW0qEEadKsF8Lg__jiI')


@bot.message_handler(commands=['start'])
def start(update: Update, context: CallbackContext, message: MessageHandler):
    markup = types.InlineKeyboardMarkup(row_width=2)

    signin = types.InlineKeyboardButton('Signin', callback_data='signin')
    signup = types.InlineKeyboardButton('Signup', callback_data='signup')


    markup.add(signin ,signup)

    bot.send_message(message.chat.id, f'Welcome {message.chat.first_name}, I Hope You Will Have Nice Time With Me!', reply_markup=markup)

    msg = bot.send_message(message.chat.id, "Click again please: /start")
    bot.register_next_step_handler(msg, next)

    help5(update, context)


def next(message):
    try:
        msg = bot.send_message(message.chat.id, 'It is next')
        # bot.reply_to(message, "its late...")
        bot.register_next_step_handler(msg, nextc)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def nextc(message):
    bot.send_message(message.chat.id, 'It is nextc')

def help5(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('finally!!!!!')




@bot.message_handler(commands=['quiz'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    num1 = types.InlineKeyboardButton('100', callback_data='answer_iron')
    num2 = types.InlineKeyboardButton('39', callback_data='answer_cotton')
    num3 = types.InlineKeyboardButton('14', callback_data='answer_same')
    no_answer = types.InlineKeyboardButton('no answer ', callback_data='no_answer')

    markup.add(num1 ,num2, num3, no_answer)

    bot.send_message(message.chat.id, '2*7 = ?', reply_markup=markup)
    msg = bot.send_message(message.chat.id, "Wow redirecting")

    bot.register_next_step_handler(msg, next)



@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.data:
        if callback.data == 'signin':
            # Signin.login()
            # bot.reply_to(callback.message, "that is my chat")
            message = bot.send_message(callback.message.chat.id, 'that is my chat')
            bot.register_next_step_handler(message, next)
        elif callback.data == 'signup':
            # Signup.register()
            bot.send_message(callback.message.chat.id, 'You Clicked Signup')


bot.polling()
# bot.enable_save_next_step_handlers(delay=2)

# # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# # WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

# bot.infinity_polling()


class Signup:
    def __init__(message,self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
    def register(message,self):
        try:
            print("-------------------Registration Page-------------------")

            f1 = open(f"{self.username}","x")


            with open(f"{self.username}","a") as file:
                file.write(f'{self.username},{self.password}\n')
            
            print("Registration Successful!")
            print("")
            x = Signin()
            x.login()
        except:
            print("There are problem, be sure be safe!!")



class Signin:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
    def login(self):
        print("-------------------Login Page-------------------")
        try:
            with open(f"{self.username}","r") as file:
                for line in file:
                    stored_username,stored_password = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        print("It is Ok!")
                        Signin.select(self)
            print("")
        except:
            print("There is no such file or you may miss the wright username or password information!\nPlease be register!")
            All.all(self)
        

    def select(self):
        print("End This is Select!!!")



class All:
    def all(self):
        try:
            print("1.signin\n2.signup\n3.exit")
            number = int(input("Enter a number: "))

            match number:
                case 1:
                    x = Signin()
                    x.login()
                case 2:
                    x = Signup()
                    x.register()
                case 3:
                    exit
                case _:
                    print("Please follow the above guide")
                    all()
        except:
            print("Incorrect input, be sure be safe!!!")
            All.all(self)

# x = All()
# x.all()






