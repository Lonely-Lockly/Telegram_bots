from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# Импортируем нужные компоненты

# Функция, которая соединяется с платформой Telegram, "тело" бота

def main():
    updater = Updater("498747935:AAHANRICU65KYR1E-tcXjpMUMqrj47whGR8")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("wordcount", word_accounting))
    updater.start_polling()
    updater.idle()

def word_accounting(bot, update):
    input_text = update.message.text     
    input_text = input_text.replace("/wordcount", "")
#   print(input_text)
    words = input_text.split()
    return_text = len(words)
    print(words)
    
    if len(input_text.split()) >= 1:
        print(return_text)
    elif len(input_text.split()) == 0:
        update.message.reply_text("Enter something!")

    if "'" in input_text or "!" in input_text or "\"" in input_text or "?" in input_text:        
    # for quotation marks in quotation marks: either '"' or "'" or "\""
        update.message.reply_text("Enter your text w/o quotation/punctuation marks!")
    
    print(input_text)
    forbidden_word = ["Devil", "damn", "sucks"]
    for word in words:
        if word in forbidden_word:
            update.message.reply_text("Do not swear!")

    update.message.reply_text(return_text)

# Вызываем функцию - эта строчка запускает бота
main()