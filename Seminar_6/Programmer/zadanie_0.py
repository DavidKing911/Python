# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

def check(s: str) -> str:
    count_1 = 0
    count_2 = 0
    for symbol in s:
        if symbol.isalpha():
            print('Неправильный ввод: нужны числа')
            exit()
    for i in range(len(s)):
        if s[i] == '(':
            count_1 += 1
        if s[i] == ")":
            count_2 += 1
    if count_1 != count_2:
        print("Некорректная запись скобок")    
        exit()
    if s[-1] == '+' or s[-1] == '-' or s[-1] == '*' or s[-1] == '/':
        print("Недостаточно числовых данных")
        exit()
    return s

def parse(s: str) -> list:
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        elif symbol in ['(', ')']:
            if digit:
                result.append(float(digit))
                digit = ""
            result.append(symbol)
        else:
            if digit:
                result.append(float(digit))
            digit = ""
            result.append(symbol)
    if digit:
        result.append(float(digit))
    if result[0] == '-':
        result.remove(result[0])
        result[0] = -result[0]
    return result

def calculator(lst: list) -> float:
    result = 0.0
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

def brackets(lst: list) -> list:
    while '(' in lst:
        close = lst.index(')')
        temp_lst = [y for x, y in zip(lst[:close], list(range(close-1))) if x == '(']
        open = temp_lst[-1]        
        lst = lst[:open] + [calculator(lst[open + 1: close])] + lst[close + 1:]
    return lst

expression = '(2+((5-3)*(16-14)))/3'
x = ''.join(expression.split())
result = brackets(parse(check(x)))
print(calculator(result))