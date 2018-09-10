from telegram.ext import Updater

API_KEY = '688721336:AAFy8ftMA6UZlFumVUSncQGMm79NAuHGJbA'

def main():
    mybot = Updater(API_KEY)
    mybot.start_polling()
    mybot.idle()
       
main()       