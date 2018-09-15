from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import logging

logging.basicConfig(format = '%(name)s - %(asctime)s - %(levelname)s - %(message)s',
 level = logging.INFO ,
 filename = 'bot.log')

API_KEY = os.environ.get("API_KEY")

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    logging.info(text)
    value_update = 'Value of variable update = {}'.format(update)
    print(value_update)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(API_KEY)
    logging.info('Bot running')

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user ))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
