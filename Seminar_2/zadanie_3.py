# Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число: "))
def sequence(num):
    summa = 0
    array = []
    for i in range(1, num + 1):
        number = (1 + 1/i)**i
        summa += number 
        array.append(f'{i}: {round(summa + i)}')
    return array

print(f"Для n = {n}: {sequence(n)}")