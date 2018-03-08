from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def calculator(bot, update):
    case = update.message.text     
    case = case.replace('/calc ', '')
#    print(case)

    all_nums = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, 
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10}

    case = all_nums.get(all_nums)
#    print(case)

    all_operators = {"плюс": "+", "минус": "-", "умножить на ": "*", "разделить на ": "/"}

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

        for n in all_operators:
        
            if n in case: 
                case = case.split()

                answer = ('{} плюс {} равно '.format(a, b, (add(a, b))))
                answer = ('{} минус {} равно '.format(a, b, (sub(a, b))))
                answer = ('{} умножить на {} равно '.format(a, b, (multi(a, b))))
                try:
                    answer = ('{} разделить на {} равно '.format(a, b, (div(a, b))))
                except ZeroDivisionError:
                    update.message.reply_text('Division by zero has no meaning! Try another number!')
            else:
                update.message.reply_text('Make sure you enter a math case!')

    update.message.reply_text(answer)

def main():
    updater = Updater("498747935:AAHANRICU65KYR1E-tcXjpMUMqrj47whGR8")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('calc', calculator))
    updater.start_polling()
    updater.idle()

main()