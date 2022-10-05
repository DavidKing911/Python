import calculator as cal
import logs
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

TOKEN = "5771556563:AAEwUt3cWJpnuacXoYQ_R7bzrlocKo8N3xg"

list_numbers = []

CALC, COMPL_CALC, RATIO_CALC, SIGN = range(4)

def start(update, _):
    """
    Начало работы бота
    """
    logs.logger('Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2: ', 'Ждем ответ.')
    update.message.reply_text('Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2: ')
    return CALC

def calc(update, _):
    """
    Выбор калькулятора
    """
    text = update.message.text
    if text.isdigit():
        num = int(text)
    if num == 1:
        logs.logger('Введено значение: ', num)
        update.message.reply_text('Введите первое рациональное число: ')
        return RATIO_CALC
    elif num == 2:
        logs.logger('Введено значение: ', num)
        update.message.reply_text('Введите первое комплексное число (через пробел): ')
        return COMPL_CALC
    logs.logger(f'Сделан неверный выбор - {text}. Повторный запрос. ', 'False')
    update.message.reply_text('Вы сделали неверный выбор. Выберите правильно: ')
    return CALC

def ratio_calc(update, _):
    """
    Калькулятор рациональных чисел
    """
    global list_numbers
    text = update.message.text
    try:
        if text == '0' or float(text):
            list_numbers.append(float(text))
        if len(list_numbers) == 1:
            logs.logger(f'Введено {len(list_numbers)} рациональное число: ', 'Ok')
            update.message.reply_text('Введите второе рациональное число: ')
            return RATIO_CALC
        else:
            logs.logger(f'Введено {len(list_numbers)} рациональное число: ', 'Ok')
            update.message.reply_text('Введите операцию над числами: ')
            cal.init_ratio(list_numbers[0], list_numbers[1])
            return SIGN
    except ValueError:
        logs.logger(f'Сделан неверный выбор. Повторный запрос. ', 'False')
        update.message.reply_text('Вы сделали неверный выбор. Выберите правильно: ')
        return RATIO_CALC

def compl_calc(update):
    """
    Калькулятор комплексных чисел
    """
    global list_numbers
    text = update.message.text
    arg = text.split(' ')
    try:
        if (arg[-2] == '0' and arg[-2] == '0') or (arg[-2] == '0' and float(arg[-1])) or (float(arg[-2]) and arg[-1] =='0') or float(arg[-2]) and float(arg[-1]):
            if len(list_numbers)<= 2:
                list_numbers.append(float(arg[-2]))
                list_numbers.append(float(arg[-1]))
                logs.logger(f'Введено {len(list_numbers)} комплексное число: ', list_numbers)
        if len(list_numbers)< 4:
            update.message.reply_text('Введите второе комплексное число (через пробел): ')
            return COMPL_CALC
        if len(list_numbers) == 4:
            logs.logger(f'Введено {len(list_numbers)} комплексное число: ', list_numbers)
            update.message.reply_text('Введите операцию над числами: ')
            cal.init_compl(list_numbers[0], list_numbers[1], list_numbers[2], list_numbers[3])
            return SIGN
    except ValueError:
        logs.logger(f'Сделан неверный выбор. Повторный запрос. ','False')
        update.message.reply_text('Вы сделали неверный выбор. Выберите правильно: ')
        return COMPL_CALC

def sign(update, _):
    """
    Выбор операции
    """
    global list_numbers
    text = update.message.text
    if text == '+':
        result = cal.sum()
    elif text == '-':
        result = cal.sub()
    elif text == '*':
        result = cal.mult()
    elif text == '/':
        result = cal.div()
    else:
        logs.logger(f'Нужно ввести знак операции ','False')
        update.message.reply_text('Выберите правильно!')
        return SIGN
    data_log = str(cal.x) + ' ' + text + ' ' + str(cal.y)
    update.message.reply_text(f'Решение примера: {str(cal.x)} {text} {str(cal.y)} = {result}')
    logs.logger(data_log, result)
    list_numbers = []
    return ConversationHandler.END

def cancel(_):
    """
    Остановка калькулятора
    """
    logs.logger(f'Калькулятор остановлен')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CALC: [MessageHandler(Filters.text, calc)],
            RATIO_CALC: [MessageHandler(Filters.text, ratio_calc)],
            COMPL_CALC: [MessageHandler(Filters.text, compl_calc)],
            SIGN: [MessageHandler(Filters.text, sign)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()