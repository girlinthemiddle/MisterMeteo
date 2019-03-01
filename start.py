from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bs4, requests, datetime, time, random, json
import logging
import Krasnoyarsk, Abakan, Chelny, Leningrad, Moskva,config, Music

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config.KEY)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    print("--------------------------------------------------------------------")
    print("START!!!!!")
    dp.add_handler(CommandHandler("start", start))
    print("--------------------------------------------------------------------")
    print("KRSK-YOBANA")
    #dp.add_handler(CommandHandler("krsk", krsk))
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    print("ABAKAN")
    #dp.add_handler(CommandHandler("abakan", abakan))
    print("--------------------------------------------------------------------")
    print("CHELNY")
    #dp.add_handler(CommandHandler("chelny", chelny))
    dp.add_handler(MessageHandler(Filters.text, text))


    #dp.add_handler(MessageHandler(Filters.text, text1))

    #dp.add_handler(MessageHandler(Filters.text, text2))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))
    # log all errors
    dp.add_error_handler(error)
    # Таймаут обновы
    updater.start_polling(poll_interval=2.0)
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    slowid = 'Ваш id: {}'.format(update.message.from_user.id)
    reply_keyboard = [["Погода 🌞", "🌚 Музыка"]]
    update.message.reply_text('Hello, my {}!'.format(update.message.from_user.first_name))
    update.message.reply_text(slowid, reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))


#Hi, my Mistress!!



# Сравнение по тексту
def text(bot, update):
#За погоду
    if update.message.text == 'Погода 🌞':
        weather(bot, update)
    if update.message.text == 'Красноярск':
        krsk(bot, update)
    if update.message.text == 'Усть':
        abakan(bot, update)
    if update.message.text == 'Челны':
        chelny(bot, update)
    if update.message.text == 'Москва':
        moskva(bot, update)
    if update.message.text == 'Ленинград':
        leningrad(bot, update)
#За музыка
    if update.message.text == '🌚 Музыка':
        music(bot, update)
    if update.message.text == 'Музыка':
        music(bot, update)
    if update.message.text == 'Cold':
        cold(bot, update)
    if update.message.text == 'Minimal':
        minimal(bot, update)
    if update.message.text == 'Techno':
        techno(bot, update)
    if update.message.text == 'Classical':
        classical(bot, update)
    if update.message.text == 'Epic':
        epic(bot, update)
    if update.message.text == 'Random':
        randomizem(bot, update)
    if update.message.text == '↩️':
        weather(bot, update)

def music(bot, update):
    reply_keyboard = [['Cold', 'Minimal', 'Techno'], ['Classical', 'Random', 'Epic'], ['↩️']]
    update.message.reply_text('Выбор жанра ✨', reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True))

def weather(bot, update):
    reply_keyboard = [['Усть', 'Красноярск', 'Челны'], ['Ленинград', 'Москва', 'Музыка']]
    update.message.reply_text('В каком городе показать? 🤔', reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = False, resize_keyboard = True))


# Погодкин домик
def krsk(bot, update):
    print("--------------------------------------------------------------------")
    print("4")
    update.message.reply_text(Krasnoyarsk.xxx)
    print("--------------------------------------------------------------------")
    update.message.reply_text(Krasnoyarsk.aaa)
    print("5")
    print("--------------------------------------------------------------------")
    update.message.reply_text(Krasnoyarsk.wwww)
    print("6")
    print("--------------------------------------------------------------------")
    update.message.reply_text(Krasnoyarsk.zzz)
    print("7")
    print("--------------------------------------------------------------------")
def abakan(bot, update):
    print("8")
    print("--------------------------------------------------------------------")
    update.message.reply_text(Abakan.xxx)
    print("--------------------------------------------------------------------")
    print("9")
    time.sleep(1)
    update.message.reply_text(Abakan.aaa)
    print("--------------------------------------------------------------------")
    print("10")
    time.sleep(1)
    update.message.reply_text(Abakan.wwww)
    print("--------------------------------------------------------------------")
    print("11")
    update.message.reply_text(Abakan.zzz)
    print("--------------------------------------------------------------------")
def chelny(bot, update):
    print("12")
    print("--------------------------------------------------------------------")
    update.message.reply_text(Chelny.xxx)
    print("--------------------------------------------------------------------")
    print("13")
    update.message.reply_text(Chelny.aaa)
    print("--------------------------------------------------------------------")
    print("14")
    update.message.reply_text(Chelny.wwww)
    print("--------------------------------------------------------------------")
    print("15")
    update.message.reply_text(Chelny.zzz)
    print("--------------------------------------------------------------------")
def leningrad(bot, update):
    update.message.reply_text(Leningrad.xxx)
    update.message.reply_text(Leningrad.aaa)
    update.message.reply_text(Leningrad.wwww)
    update.message.reply_text(Leningrad.zzz)
def moskva(bot, update):
    update.message.reply_text(Moskva.xxx)
    update.message.reply_text(Moskva.aaa)
    update.message.reply_text(Moskva.wwww)
    update.message.reply_text(Moskva.zzz)

#Музычкин домик
def cold(bot, update):
    update.message.reply_text(random.choices(Music.ListCold))
def minimal(bot, update):
    update.message.reply_text(random.choices(Music.ListMinimal))
def techno(bot, update):
    update.message.reply_text(random.choices(Music.ListTechno))
def classical(bot, update):
    update.message.reply_text(random.choices(Music.ListClassical))
def epic(bot, update):
    update.message.reply_text(random.choices(Music.ListEpic))
def randomizem(bot, update):
    update.message.reply_text(random.choices(Music.ListRandom))

"""
def random(bot, update):
    update.message.reply_text(random.choices(Music.ListRandom))
"""


#def echo(bot, update):
#    """Echo the user message."""
#
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

if __name__ == '__main__':
    main()
