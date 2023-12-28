from typing import Final
from telegram.ext import Application, CommandHandler, filters, ContextTypes, MessageHandler, CallbackContext, ConversationHandler

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import telebot
from telebot import types

from time import sleep

# from PIL import Image


TOKEN: Final = '6324612031:AAFZcKgoiy4Sk0U0dedrxNMADZ2SfIUj2qo'
BOT_USERNAME: Final =  '@deleted84bot'

bot = telebot.TeleBot(TOKEN)

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # await update.message.reply_text(f'Hello!!! {update.message.chat.first_name} Tanks for chatting with me! I am your assistant!!!')

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)


    lists = types.KeyboardButton('View List')
    order = types.KeyboardButton('Order')


    markup.add(lists ,order)

    # chat_id =-1002137636709

    # bot.send_message(chat_id=-1002137636709, text="Wow my Group")

    bot.send_message(update.message.chat.id, f'Hello!!! {update.message.chat.first_name}, Thanks for chatting with me! I am your assistant!!!', reply_markup=markup)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text('I am a banana! Please type sth so i can respond to you just relax!')

    # await update.message.reply_text('Hello!!! Thanks for chatting with me! I am your assistant!!!')

    bot.send_message(update.message.chat.id,f'Hello!!!, {update.message.chat.first_name} please use the below guide button!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '''
        It is the food ordering bot,
you can order your favorite food!
        '''
        )


async def viewlist_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # bot.send_photo(chat_id=1243724343, open('1145.jpg','rb'))
    # bot.reply_to(update.message, 'id num: 1')
    # await update.message.reply_photo(photo=open('images/1145.jpg', 'rb'))
    # bot.send_photo(chat_id=1243724343, photo=open('images/1145.jpg', 'rb'),caption='Hello {} id number 1 '.format(update.message.chat.first_name))
    await update.message.reply_text('please wait.....')
    # sleep(15)
    try:
        # bot.send_photo(update.message.chat_id, photo=open('images/food6.png', 'rb'),caption='id number 1 ')
        bot.send_photo(update.message.chat_id,photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699030469/food4_vajkae.jpg',caption='id number 1 ')
        bot.send_photo(update.message.chat_id,photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699030477/food2_e802dr.jpg',caption='id number 2 ')
        bot.send_photo(update.message.chat_id,photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699027697/samples/dessert-on-a-plate.jpg',caption='id number 3 ')
        bot.send_photo(update.message.chat_id,photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699031300/food1_rajsjx.jpg',caption='id number 4 ')
        # await update.message.reply_text('This is a viewlist command')
    except:
        await update.message.reply_text("Not Worked")

async def order_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text('This is a Ordering command')

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    button1 = types.KeyboardButton('1')
    button2 = types.KeyboardButton('2')
    button3 = types.KeyboardButton('3')
    button4 = types.KeyboardButton('4')
    button5 = types.KeyboardButton('🔙Back')


    markup.add(button1 ,button2,button3,button4,button5)

    bot.send_message(update.message.chat.id, 'please order from lists!', reply_markup=markup)

async def back_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_command(update, context)


#Responses

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    processed: str = update.message.text.lower()


    #First Phase
    if 'hey' in processed:
        await update.message.reply_text(f"How are doing bro! i'm fine {update.message.from_user.first_name}")
        # await update.message.from_user.send_photo(photo=open('images/1145.jpg', 'rb'))
    if 'view list' in processed:
        await viewlist_command(update, context)
    if 'order' in processed:
        await order_command(update, context)
    if '🔙back' in processed:
        await back_command(update, context)
    
    #Second Phase
    if '1' in processed:
        try:
            await update.message.reply_text('please wait.....')
            sleep(2)
            await update.message.reply_text('here is your record:')
            await update.message.reply_photo(
                'https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699030469/food4_vajkae.jpg',
                caption=
                f"""
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
"""
)
            bot.send_photo(
                chat_id=-1002137636709,
                photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699030469/food4_vajkae.jpg',
                caption=
                f"""
name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
chat_id: {update.message.chat_id}
"""
            )
        except:
            await update.message.reply_text("Nop Nop")
#         await update.message.reply_text(
# f"""
# First name:  {update.message.chat.first_name}
# User name: @{update.message.chat.username}
# """
# )
        # bot.send_message(chat_id=-1002137636709, text="Wow my Group")
#         bot.send_photo(
#             chat_id=-1002137636709,
#             photo=open('images/1145.jpg', 'rb'),
#             caption=
#             f"""
# First name:  {update.message.chat.first_name}
# User name: @{update.message.chat.username}
# """
#             )
        
    if '2' in processed:
        try:
            await update.message.reply_text('please wait.....')
            await update.message.reply_text('here is your record:')
            await update.message.reply_photo(
                photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699030477/food2_e802dr.jpg',
                caption=
                f"""
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
"""
)
            bot.send_photo(
                chat_id=-1002137636709,
                photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699030477/food2_e802dr.jpg',
                caption=
                f"""
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
chat_id: {update.message.chat_id}
"""
            )
        except:
            await update.message.reply_text("please try again!")
    if '3' in processed:
        try:
            await update.message.reply_text('please wait.....')
            await update.message.reply_text('here is your record:')
            await update.message.reply_photo(
                photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699027697/samples/dessert-on-a-plate.jpg',
                caption=
                f"""
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
"""
)
            bot.send_photo(
                chat_id=-1002137636709,
                photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699027697/samples/dessert-on-a-plate.jpg',
                caption=
                f"""
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
chat_id: {update.message.chat_id}
"""
            )
        except:
            await update.message.reply_text("please try again!")
    if '4' in processed:
        try:
            await update.message.reply_text('please wait.....')
            await update.message.reply_text('here is your record:')
            await update.message.reply_photo(
                photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699031300/food1_rajsjx.jpg',
                caption=
                f"""
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
"""
)
            bot.send_photo(
                chat_id=-1002137636709,
                photo='https://res.cloudinary.com/dpr7vgjrb/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1699031300/food1_rajsjx.jpg',
                caption=
                f"""
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
chat_id: {update.message.chat_id}
"""
            )
        except:
            await update.message.reply_text("please try again!")

    
    return f'Please {update.message.chat.first_name} Follow the guide!'
    # return f'You Entered: {text}'


async def handle_message(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            # new_text: str = text.replace(BOT_USERNAME, '').strip()
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            # response: str = handle_response(new_text)
            response = handle_response(new_text,update, context)
        else:
            return
    else:
        response = handle_response(update,context)

    print('Bot:', response)
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
    app.add_handler(CommandHandler('order', order_command))
    app.add_handler(CommandHandler('view_list', viewlist_command))
    app.add_handler(CommandHandler('back', back_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)


    #Polls the bot
    print('Polling.......')
    app.run_polling(poll_interval=5)