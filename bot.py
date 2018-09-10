from telegram.ext import Updater, CommandHandler      
from os import environ
import pprint

# Run in cmd line "source secrets.txt" before running
API_KEY = environ.get('API_KEY') 

def greet_user(bot, update):
    print('Вызван /start')
    # pprint method print a dictionary in a column
    pprint.pprint(update.to_dict())

def main():
    mybot = Updater(API_KEY)
    mydisp = mybot.dispatcher
    mydisp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()
       
main()       