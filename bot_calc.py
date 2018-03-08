from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# Импортируем нужные компоненты

def calculator(bot, update):
    case = update.message.text     
    case = case.replace('/calc ', '')
    case = case.replace('=', '')
    print(case)

    operation = ['+', '-', '/', '*']

    #Addition
    def add(a, b):
        result = a + b
        return result
     
    #Subtraction
    def sub(a, b):
        result = a - b
        return result
     
    #Division
    def div(a, b):
        result = a / b
        return result
     
    #Multiplication
    def multi(a, b):
        result = a * b
        return result

        for n in operation:
        
            if n in case: 
                case = case.split()
                num_1 = int(case)
                num_2 = int(case)

                answer = ('{} + {} = '.format(num_1, num_2,(add(num_1, num_2))))
                answer = ('{} - {} = '.format(num_1, num_2,(sub(num_1, num_2))))
                answer = ('{} * {} = '.format(num_1, num_2,(multi(num_1, num_2))))
                try:
                    answer = ('{} / {} = '.format(num_1, num_2,(div(num_1, num_2))))
                except ZeroDivisionError:
                    update.message.reply_text('Division by zero has no meaning! Try another number!')
            else:
                update.message.reply_text('Make sure you enter a math case with "+", "-", "*" or "/"!')

    update.message.reply_text(answer)

# Функция, которая соединяется с платформой Telegram, "тело" бота

def main():
    updater = Updater("498747935:AAHANRICU65KYR1E-tcXjpMUMqrj47whGR8")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('calc', calculator))
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка запускает бота
main()
