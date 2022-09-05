# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input("Введите число: ")
def amount(num):
    summa = 0
    for i in num:
        if i.isdigit():
            summa += int(i)
    return summa

print(f"Сумма цифр числа {number} -> {amount(number)}")