from telegram.ext import Updater

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def main():
    mybot = Updater('688721336:AAFy8ftMA6UZlFumVUSncQGMm79NAuHGJbA',request_kwargs=PROXY)
    mybot.start_polling()
    mybot.idle()
       
main()       