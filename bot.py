from telegram.ext import Updater,Filters,CommandHandler,MessageHandler
from handlers import start,send_weather
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN=os.getenv("TOKEN")

updater=Updater(TOKEN)
dispatcher=updater.dispatcher
def main():
    dispatcher.add_handler(CommandHandler('start',start))
    dispatcher.add_handler(MessageHandler(Filters.location,send_weather))
    updater.start_polling()
    updater.idle()


main()
