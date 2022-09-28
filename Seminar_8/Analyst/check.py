
def check_int_number(number: str) -> int:
    '''
    Поверка на целое число
    '''
    while True:
        try:
            return int(input(number))
        except ValueError:
            print('Ошибка! Должно быть целое число!')