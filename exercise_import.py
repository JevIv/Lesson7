from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
import ephem
import logging
import settings

logging.basicConfig(filename = 'bot.log', level = logging.INFO)
planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
today = date.today()
date_today = today.strftime("%Y/%m/%d")

def greet_user(update, context):
    print("Called /start")
    update.message.reply_text("Hello my darling! How are you today?")
    update.message.reply_text("Please input a name of the planet.\n Example: /planet Mars")

def talk_to_me(update,context):
    text = update.message.text.split()
    planet = text[1]
    if planet in planets:
        if planet == planets[0]:
            planet_pos = ephem.Mercury(date_today)
        elif planet == planets[1]:
            planet_pos = ephem.Venus(date_today)
        elif planet == planets[2]:
            planet_pos = ephem.Earth(date_today)
        elif planet == planets[3]:
            planet_pos = ephem.Mars(date_today)
        elif planet == planets[4]:
            planet_pos = ephem.Jupiter(date_today)
        elif planet == planets[5]:
            planet_pos = ephem.Saturn(date_today)
        elif planet == planets[6]:
            planet_pos = ephem.Uranus(date_today)
        elif planet == planets[7]:
            planet_pos = ephem.Neptune(date_today)
        constellation = ephem.constellation(planet_pos)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text("Wrong planet")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))    #dobavljaju obrabot4ik
    dp.add_handler(CommandHandler("planet", talk_to_me))
    logging.info("Bot started")
    mybot.start_polling()    #proverjaet obnovleniaj dlja bota
    mybot.idle()           #krutisj postojannno


if __name__=="__main__":
    main()
