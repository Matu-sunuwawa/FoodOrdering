from typing import Final
from telegram.ext import Application, CommandHandler, filters, ContextTypes, MessageHandler, CallbackContext, ConversationHandler

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import telebot
from telebot import types

from time import sleep

# from PIL import Image


TOKEN: Final = '6346028122:AAFkwwcBRxq2WC7U5-uijvWBLwXBVkK2szc'
BOT_USERNAME: Final =  '@order_the_foodbot'

bot = telebot.TeleBot(TOKEN)

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # await update.message.reply_text(f'Hello!!! {update.message.chat.first_name} Tanks for chatting with me! I am your assistant!!!')

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)


    lists = types.KeyboardButton('View List')
    order = types.KeyboardButton('Order')
    message = types.KeyboardButton('Leave Message')
    contact = types.KeyboardButton('Contact Us')


    markup.add(lists ,order,message,contact)

    # chat_id =-1002137636709

    # bot.send_message(chat_id=-1002137636709, text="Wow my Group")

    bot.send_message(update.message.chat.id, f'Hello!!! {update.message.chat.first_name}, Thanks for chatting with me! I am your assistant!!!', reply_markup=markup)

async def origin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)


    lists = types.KeyboardButton('View List')
    order = types.KeyboardButton('Order')
    message = types.KeyboardButton('Leave Message')
    contact = types.KeyboardButton('Contact Us')


    markup.add(lists ,order,message,contact)

    # chat_id =-1002137636709

    # bot.send_message(chat_id=-1002137636709, text="Wow my Group")

    bot.send_message(update.message.chat.id, 'Main Menu:', reply_markup=markup)

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
    try:
        await update.message.reply_text("""
1.Baked goods.
2.Cereals.
3.Dairy products.
4.Edible plants.
5.Edible fungi.
6.Edible nuts and seeds.
7.Legumes.
8.Meat
""")
    except:
        await update.message.reply_text("Not Worked")

async def order_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    markup = types.ReplyKeyboardMarkup(row_width=8,resize_keyboard=True)

    button1 = types.KeyboardButton('1')
    button2 = types.KeyboardButton('2')
    button3 = types.KeyboardButton('3')
    button4 = types.KeyboardButton('4')
    button5 = types.KeyboardButton('5')
    button6 = types.KeyboardButton('6')
    button7 = types.KeyboardButton('7')
    button8 = types.KeyboardButton('8')
    button9 = types.KeyboardButton('🔝Main Menu')


    markup.add(button1 ,button2,button3,button4,button5,button6,button7,button8,button9)

    bot.send_message(update.message.chat.id, 'please order from lists!', reply_markup=markup)

async def leave_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)

    cancel = types.KeyboardButton('🚫Cancel')


    markup.add(cancel)

    bot.send_message(update.message.chat.id, 'please feel free to write down your comment!', reply_markup=markup)

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is the contact command!')

async def idnum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('here is your record:')
    a = {
        '1':'Baked goods',
        '2':'Cereals',
        '3':'Dairy products',
        '4':'Edible plants',
        '5':'Edible fungi',
        '6':'Edible nuts and seeds',
        '7':'Legumes',
        '8':'Meat'
    }
    b = '1,2,3,4,5,6,7,8'
    c = b.split(',')
    for i in c:
        if update.message.text == i:
            print(a[i])
            await update.message.reply_text(
                f"""
Your order: id num {i}({a[i]})
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
chat_id: {update.message.chat_id}
"""
)
            bot.send_message(
                chat_id=1243724343,
                text=
                f"""
Your order: id num {i}({a[i]})
First name:  {update.message.chat.first_name}
User name: @{update.message.chat.username}
chat_id: {update.message.chat_id}
"""
            )
            break

async def replytouser_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userchatid: int = update.message.text

    bot.send_message(chat_id=userchatid,text="""
Thanks for using our product
""")

async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await origin_command(update,context)

async def main_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await origin_command(update, context)


#Responses

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    processed: str = update.message.text.lower()
    letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    split = letters.split(',')
    chatid = '1,2,3,4,5,6,7,8,9,0'
    split2 = chatid.split(',')
    commands = ['view list','order','leave message','contact us','🚫cancel','🔝main menu']
    found = ''
    print(processed)

    #First Phase
    if 'hey' in processed:
        await update.message.reply_text(f"How are doing bro! i'm fine {update.message.from_user.first_name}")
    elif 'view list' in processed:
        await viewlist_command(update, context)
    elif 'order' in processed:
        await order_command(update, context)
    elif 'leave message' in processed:
        await leave_command(update, context)
    elif 'contact us' in processed:
        await contact_command(update, context)
    elif '🚫cancel' in processed:
        await cancel_command(update, context)
    elif '🔝main menu' in processed:
        await main_command(update, context)
    elif processed in commands:
        return
    else:
        for i in split:
            if i in processed:
                await origin_command(update, context)
                bot.send_message(chat_id=1243724343,text=f"""
{processed}
""")
                break
    try:
        convert = int(processed)
        for j in split2:
            if j in processed:
                if bot.get_chat(convert):
                    await replytouser_command(update,context)
                    break
    except:
        pass
    
    #Second Phase
    b = '1,2,3,4,5,6,7,8'
    c = b.split(',')
    for i in c:
        if i == update.message.text:
            try:
                await idnum_command(update,context)
                break
            except:
                await update.message.reply_text("Please try again")

    
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

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)


    #Polls the bot
    print('Polling.......')
    app.run_polling(poll_interval=2)