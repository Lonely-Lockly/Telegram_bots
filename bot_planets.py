from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# Импортируем нужные компоненты

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота

def main():
    updater = Updater("498747935:AAHANRICU65KYR1E-tcXjpMUMqrj47whGR8")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("planet", planet_location))
    updater.start_polling()
    updater.idle()

#def planet_location(bot, update):
#    planet = 'Вызван /planet'
#    planet = update.message.text 
#    print(planet)

#    date = datetime.datetime.now()
#    planet = ephem.Mars(date)
#    ephem.Mars()
#    constellation = ephem.constellation(planet)
#    update.message.reply_text(constellation)
    
def planet_location(bot, update):
    planet = update.message.text 
    planet = planet.replace('/planet ', '')
    print(planet)

    solar_system_planet = {"Mercury": ephem.Mercury, "Venus": ephem.Venus, 
    "Mars": ephem.Mars, "Jupiter": ephem.Jupiter, "Saturn": ephem.Saturn,
    "Uranus": ephem.Uranus, "Neptune": ephem.Neptune, "Pluto": ephem.Pluto}
    
    date = datetime.datetime.now()
    planet = solar_system_planet.get(planet)
    print(planet)
    constellation = planet(date)
    print(constellation)
    result = ephem.constellation(constellation)    
    print(result)
    update.message.reply_text(result)

# Вызываем функцию - эта строчка запускает бота
main()