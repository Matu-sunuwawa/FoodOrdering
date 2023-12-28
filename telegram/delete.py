from typing import Final
from telegram.ext import Application, CommandHandler, filters, ContextTypes, MessageHandler, CallbackContext, ConversationHandler

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import telebot
from telebot import types


TOKEN: Final = '6324612031:AAFZcKgoiy4Sk0U0dedrxNMADZ2SfIUj2qo'
BOT_USERNAME: Final =  '@deleted84bot'

bot = telebot.TeleBot(TOKEN)

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # reply_keyboard = [["Boy", "Girl", "Other"]]

    await update.message.reply_text('Hello!!! Tanks for chatting with me! I am your assistant!!!')
    await update.message.reply_text("There is your info:")
    await update.message.reply_text(f'Channel_Chat_Created: {update.message.channel_chat_created}')
    await update.message.reply_text(f'First_Name: {update.message.chat.first_name}')
    await update.message.reply_text(f'UserName: {update.message.chat.username}')
    # await update.message.reply_text(
    #     reply_markup=ReplyKeyboardMarkup(
    #         reply_keyboard, one_time_keyboard=True, input_field_placeholder="Boy or Girl?"
    #     ),
    # )
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    # signin = types.KeyboardButton('Signin', callback_data='signin')
    # signup = types.KeyboardButton('Signup', callback_data='signup')
    signin = types.KeyboardButton('Signin')
    signup = types.KeyboardButton('Signup')


    markup.add(signin ,signup)

    bot.send_message(update.message.chat.id, f'Welcome {update.message.chat.first_name}, I Hope You Will Have Nice Time With Me!', reply_markup=markup)

    await help5(update, context)

async def help5(update:Update, context: CallbackContext):
    await update.message.reply_text('this is reply')
    # processed: str = update.message.text.lower()

    # if 'signin' in processed:
    #     return 'Owkay!! signin!!!'
    # if 'signup' in processed:
    #     return 'Owkay!! signup!!!'
    
    # # return 'I don not understand'
    # return f'You Entered: {update.message.text}'




async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text('I am a banana! Please type sth so i can respond to you just relax!')

    await update.message.reply_text('Hello!!! Tanks for chatting with me! I am your assistant!!!')
    await update.message.reply_text("There is your info:")

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    signin = types.KeyboardButton('Nextjs')
    signup = types.KeyboardButton('Reactjs')


    markup.add(signin ,signup)

    bot.send_message(update.message.chat.id, f'Welcome {update.message.chat.first_name}, I Hope You Will Have Nice Time With Me!', reply_markup=markup)

    await help5(update, context)

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a register command')
    await update.message.reply_text('Please fill out username:')
    username = update.message.text.lower().capitalize()
    await update.message.reply_text('Please fill out password:')
    password = update.message.text.lower().capitalize()
    await update.message.reply_text(f'Your info: username: {username} password: {password}')
    await update.message.forward

async def signup_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text('This is a Signup command')

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    signin = types.KeyboardButton('first1')
    signup = types.KeyboardButton('first2')


    markup.add(signin ,signup)

    bot.send_message(update.message.chat.id, f'Welcome {update.message.chat.first_name}, I Hope You Will Have Nice Time With Me!', reply_markup=markup)



#Responses

async def hhh(update: Update,context: CallbackContext):
    await update.message.reply_text('Reply Text')


async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    processed: str = update.message.text.lower()

    # if 'b':
    #     return f'you entered: {text}'
    # if 'hello' in processed:
    #     return 'Hey there!'
    # if 'how are you' in processed:
    #     return 'I am good'
    # if 'i love python' in processed:
    #     return 'Remember to subscribe'
    if 'signin' in processed:
        return 'Owkay!! signin!!!'
        # return h6()
    if 'signup' in processed:
        # return 'Owkay!! signup!!!'
        await register_command(update, context)
    
    return 'I don not understand.....'
    # return f'You Entered: {text}'

# def handle_response(text: str) -> str:
#     processed: str = text.lower()

#     # if 'b':
#     #     return f'you entered: {text}'
#     # if 'hello' in processed:
#     #     return 'Hey there!'
#     # if 'how are you' in processed:
#     #     return 'I am good'
#     # if 'i love python' in processed:
#     #     return 'Remember to subscribe'
#     if 'signin' in processed:
#         return 'Owkay!! signin'
#         # return h6()
#     if 'signup' in processed:
#         # return 'Owkay!! signup'
#         return signup_command()
    
#     return 'I don not understand'
#     # return f'You Entered: {text}'


def h6():
    # types.ReplyKeyboardRemove()

    return 'Alah wekber'

async def handle_message(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        # response: str = handle_response(text)
        # response: str = handle_response(update,context)
        response = handle_response(update,context)
        # response2: str = hhh(update,context)

    print('Bot:', response)
    # print('Bot:', response2)
    # await update.message.reply_text(response)
    await response


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    print('Starting the bot....')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('Signup', signup_command))
    app.add_handler(CommandHandler('Signup', register_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)


    #Polls the bot
    print('Polling.......')
    app.run_polling(poll_interval=5)


#TELEGRAM BOT DETAIL INFO
# Update Update(message=Message(channel_chat_created=False, chat=Chat(first_name='Deleted Account', id=1243724343, type=<ChatType.PRIVATE>, username='Matusala'), 
#                               date=datetime.datetime(2023, 10, 31, 12, 0, 34, tzinfo=datetime.timezone.utc), 
#                               delete_chat_photo=False, entities=(MessageEntity(length=5, offset=0, type=<MessageEntityType.BOT_COMMAND>),),
#                               from_user=User(first_name='Deleted Account', id=1243724343, is_bot=False, language_code='en', username='Matusala'), 
#                               group_chat_created=False, message_id=114, supergroup_chat_created=False, text='/help')
#                               , update_id=18106981) caused error Timed out


#Sending Message
# https://api.telegram.org/bot6324612031:AAFZcKgoiy4Sk0U0dedrxNMADZ2SfIUj2qo/sendMessage?chat_id=1243724343&text=Hello
# https://api.telegram.org/bot6773737938:AAEFlhrkhlpuAqrBIW0qEEadKsF8Lg__jiI/getUpdates
#"message":{"message_id":22,"from":{"id":1243724343,"is_bot":false,"first_name":"Deleted Account","username":"Matusala","language_code":"en"},"chat":{"id":-1002137636709,"title":"Register_new","type":"supergroup"},"date":1698927264,"text":"hey"}}]}
# {"ok":true,"result":[{"update_id":18107256,
# "message":{"message_id":22,"from":{"id":1243724343,"is_bot":false,"first_name":"Deleted Account","username":"Matusala","language_code":"en"},"chat":{"id":-1002137636709,"title":"Register_new","type":"supergroup"},"date":1698927264,"text":"hey"}},{"update_id":18107257,
# "message":{"message_id":23,"from":{"id":1243724343,"is_bot":false,"first_name":"Deleted Account","username":"Matusala","language_code":"en"},"chat":{"id":-1002137636709,"title":"Register_new","type":"supergroup"},"date":1698927438,"text":"hey"}},{"update_id":18107258,
# "message":{"message_id":24,"from":{"id":1243724343,"is_bot":false,"first_name":"Deleted Account","username":"Matusala","language_code":"en"},"chat":{"id":-1002137636709,"title":"Register_new","type":"supergroup"},"date":1698927458,"text":"hey"}}]}
#https://api.telegram.org/bot6324612031:AAFZcKgoiy4Sk0U0dedrxNMADZ2SfIUj2qo/sendMessage?chat_id=1243724343&text=Hello%20world

#TELEGRAM BOT BUTTONS
# class telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=None, 
#                                    one_time_keyboard=None, selective=None, input_field_placeholder=None, 
#                                    is_persistent=None, *, api_kwargs=None)



#REGISTRATION TRIAL
# REGISTRATION,FIRST,AGE=range(3)
# def start(bot,update)->int:
#     print('user started the bot')    
#     user = update.message.from_user
#     bot.sendphoto(chatid=update.message.chatid, photo = 'https://icon-library.com/images/bot-icon/bot-icon-5.jpg',caption='Hello {} this is econ bot '.format(user.first_name))

#     return REGISTRATION

# def register(bot, update):
#     bot.sendmessage(chatid=update.message.chatid, text="Welcome! Please enter your name")
#     return FIRST  # (1)
# def first(bot, update):  # (2)
#     user = update.message.from_user
#     name = update.message.text
#     user.data.user.id = name  # (3)
#     reply = "Thanks for registering {}!\n Enter your age".format(name)  # (4)
#     bot.sendmessage(chatid=update.message.chatid, text=reply)
#     return AGE  # (5)
# def age(bot, update):  # (6)  
#     age = int(update.message.text)
#     user = update.message.from_user
#     if age < 18:     # (7)  
#       bot.sendmessage(chatid=update.message.chat.id, text="Sorry you are too young to register")   
#     else:     
#      user.data.user.obj = age     
#      bot.sendmessage(chatid=update.message.chat.id, text="Registration successful!")     
     
#     return ConversationHandler.END  # (8)



# Update Update(message=Message(channel_chat_created=False, chat=Chat(first_name='Deleted Account', id=1243724343, type=<ChatType.PRIVATE>, username='Matusala'), date=datetime.datetime(2023, 11, 2, 19, 19, 42, tzinfo=datetime.timezone.utc), delete_chat_photo=False, from_user=User(first_name='Deleted Account', id=1243724343, is_bot=False, language_code='en', username='Matusala'), group_chat_created=False, message_id=453, supergroup_chat_created=False, text='View List'), update_id=596816204) caused error HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot6324612031:AAFZcKgoiy4Sk0U0dedrxNMADZ2SfIUj2qo/sendPhoto?chat_id=1243724343&caption=id+number+1+ (Caused by SSLError(SSLWantWriteError(3, 'The operation did not complete (write) (_ssl.c:2423)')))


#OPEN AI VALIDATE NUMBER:

# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# # Define states for the conversation
# SELECTING_OPTION, GETTING_NUMBER = range(2)

# # Dictionary to store user data
# user_data = {}

# # Define a command to start the conversation
# def start(update, context):
#     update.message.reply_text("Please send me a number, and I will convert it to an integer.")
#     return SELECTING_OPTION

# # Define a function to check if the input is a valid number
# def is_number(text):
#     try:
#         int(text)
#         return True
#     except ValueError:
#         return False

# # Handle the user's response
# def get_number(update, context):
#     user_input = update.message.text
#     if is_number(user_input):
#         number = int(user_input)
#         update.message.reply_text(f"The integer value of {user_input} is {number}.")
#     else:
#         update.message.reply_text("That's not a valid number. Please send me a valid number.")
#         return SELECTING_OPTION
#     return ConversationHandler.END

# # Create a conversation handler
# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler('start', start)],
#     states={
#         SELECTING_OPTION: [MessageHandler(Filters.text & ~Filters.command, get_number)],
#     },
#     fallbacks=[],
#     allow_reentry=True
# )

# def main():
#     # Replace 'YOUR_BOT_TOKEN' with your actual bot token
#     updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(conv_handler)

#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()
