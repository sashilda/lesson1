from telegram.ext import Updater


def main():
    mybot = Updater('688721336:AAFy8ftMA6UZlFumVUSncQGMm79NAuHGJbA')
    mybot.start_polling()
    mybot.idle()
       
main()       