import check as ch

def data():
    """
    Ввод данных
    """
    return input("Введите ФИО: "), input("Введите дату рождения: "), \
        input("Введите профессию: "), input("Введите номер телефона: "), input("Введите з/п в рублях: ")

def choice():
    """
    Выбор операции
    """
    num = ch.check_int_number("Импорт данных - 1\nЭкспорт данных - 2\n")
    return num