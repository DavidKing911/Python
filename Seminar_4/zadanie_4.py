# Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
import sympy as sm

def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

def rand():
    '''
    Генерация случайного числа
    '''
    rnd = random.randint(1, 100)
    return rnd

number = abs(get_number("Введите натуральное число: "))

def polynomial(k):
    '''
    Создание многочлена
    '''
    x = sm.Symbol("x")
    polynom = 0
    for i in range(-k, 0):
        polynom += rand()*x**abs(i)
    polynom += rand()
    return polynom

print(f"k = {number} => {polynomial(number)} = 0")