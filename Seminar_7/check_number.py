def check_int_number(number:str) -> int:
    '''
    Поверка на целое число
    '''

    while True:
        try:
            num = int(input(number))
            return num
        except ValueError:
            print('Ошибка! Должно быть целое число!')

def check_float_number(number:str) -> float:
    '''
    Поверка на дробное число
    '''

    while True:
        try:
            num = float(input(number))
            return num
        except ValueError:
            print('Ошибка! Должно быть дробное число!')

def check_symbol(symbol:str) -> str:
    '''
    Поверка знака действия
    '''

    while True:
        try:
            sym = input(symbol)
            if sym in '+-*/':
                return sym
        except ValueError:
            print('Ошибка! Должен быть знак действия ("+", "-", "*", "/")!')

def check_calc(digit:str) -> int:
    '''
    Поверка выбора калькулятора
    '''

    while True:
        try:
            calc_choice = input(digit)
            if calc_choice == '1':
                return int(calc_choice)
            elif calc_choice == '2':
                return int(calc_choice)
        except ValueError:
            print('Ошибка! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2')