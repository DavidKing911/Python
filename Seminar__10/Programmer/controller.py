import logs, operation, time
from configs import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

CHOICE, ADD, SEARCH, VIEW, SERNAME, PHONE_NUMBER, COMMENT = range(7)

def start(update, _):
    """
    Начало работы бота
    """
    reply_keyboard = [['📔 ADD','🕵‍♂ SEARCH', '📚 VIEW ALL','🚪 EXIT']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Выберите операцию, которую хотите совершить с телефонной книгой?', reply_markup=markup_key)
    return CHOICE

def choice(update, _):
    """
    Выбор операции пользователя
    """
    text = update.message.text
    keyboard_remove = ReplyKeyboardRemove()
    logs.logger("Пользователь выбрал операцию", text)
    if text == '📔 ADD':
        update.message.reply_text('Введите имя', reply_markup=keyboard_remove)
        return ADD
    if text == '🕵‍♂ SEARCH':
        update.message.reply_text('Введите значение, которое поможет мне найти нужные вам данные', reply_markup=keyboard_remove)
        return SEARCH
    if text == '📚 VIEW ALL':
        update.message.reply_text('Это секретные данные, но если у вас есть пароль для просмотра, то введите пароль', reply_markup=keyboard_remove)
        update.message.reply_text('PS: пароль - 12345')
        return VIEW
    if text == '🚀 CONTINUE':
        return start(update, _)
    if text == '🚪 EXIT':
        update.message.reply_text(f'Приятно было иметь с вами дело, {update.effective_user.first_name}', reply_markup=keyboard_remove)
        return cancel()

def add(update, _):
    global list_add
    list_add = []
    text = update.message.text
    list_add.append(text)
    update.message.reply_text('Введите фамилию')
    return SERNAME

def sername(update, _):
    text = update.message.text
    list_add.append(text)
    update.message.reply_text('Введите номер телефона')
    return PHONE_NUMBER

def phone_number(update, _):
    text = update.message.text
    list_add.append(text)
    update.message.reply_text('Введите комментарий')
    return COMMENT

def comment(update, _):
    text = update.message.text
    list_add.append(text)
    logs.logger("Пользователь добавил данные", list_add)
    operation.write_csv(list_add)
    update.message.reply_text('Данные добавлены')
    time.sleep(1)
    reply_keyboard = [['🚀 CONTINUE','🚪 EXIT']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Вы хотите продолжить операции с телефонной книгой или желаете окончить сеанс?', reply_markup=markup_key)
    return CHOICE

def search(update, _):
    text = update.message.text
    result = operation.search_csv(text)
    resultat = "\n\n".join(result)
    if result == 'Данные осутствуют':
        update.message.reply_text(result)
    else:
        update.message.reply_text(f'Вот всё, что я смог найти в базе данных:\n\n{resultat}')
    time.sleep(1)
    reply_keyboard = [['🚀 CONTINUE','🚪 EXIT']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Вы хотите продолжить операции с телефонной книгой или желаете окончить сеанс?', reply_markup=markup_key)
    return CHOICE

def view(update, _):
    text = update.message.text
    result = operation.read_csv()
    if text == '12345':
        update.message.reply_text(f'Пароль верный)')
        resultat = '\n\n'.join(str(l) for l in result)
        time.sleep(1)
        update.message.reply_text(f'Вот все данные, которые присутсвуют в базе данных:\n\n{resultat}')
    else:
        update.message.reply_text(f'К сожалению, пароль не верный)')
    time.sleep(1)
    reply_keyboard = [['🚀 CONTINUE','🚪 EXIT']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Вы хотите продолжить операции с телефонной книгой или желаете окончить сеанс?', reply_markup=markup_key)
    return CHOICE

def cancel():
    """
    Завершение сеанса
    """
    logs.logger(f'Пользователь вышел', 'THE END')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            ADD: [MessageHandler(Filters.text, add)],
            SEARCH: [MessageHandler(Filters.text, search)],
            VIEW: [MessageHandler(Filters.text, view)],
            SERNAME: [MessageHandler(Filters.text, sername)],
            PHONE_NUMBER: [MessageHandler(Filters.text, phone_number)],
            COMMENT: [MessageHandler(Filters.text, comment)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()