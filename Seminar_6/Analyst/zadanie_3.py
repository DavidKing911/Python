# Найти расстояние между двумя точками пространства(числа вводятся через пробел)
def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

def find_distance():
    x1 = get_number("Введите х1: ")
    y1 = get_number("Введите у1: ")
    x2 = get_number("Введите х2: ")
    y2 = get_number("Введите у2: ")
    s = lambda x1, x2, y1, y2: ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    print(f"{round(s(x1, x2, y1, y2), 2)} - расстояние между точками")

find_distance()