import check_number as f

def rational_number(number:str) -> float:
    '''
    Ввод рационального числа
    '''

    num = f.check_float_number(number)
    return num

def complex_number(number:str) -> complex:
    '''
    Ввод комплексного числа
    '''

    num = f.check_int_number(number)
    return num

def operation(oper:str) -> str:
    '''
    Ввод операции
    '''
    symb = f.check_symbol(oper)
    return symb

def choice_calc(number:str) -> int:
    '''
    Выбор калькулятора
    '''

    calc = f.check_calc(number)
    return calc