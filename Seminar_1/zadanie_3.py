# Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quarter():
    x = input("Введите х: ")
    y = input("Введите y: ")
    while x.lstrip("-").isdigit() is not True or y.lstrip("-").isdigit() is not True:
        print("Ошибка!")
        x = input("Введите х: ")
        y = input("Введите y: ")
    x = int(x)
    y = int(y)
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print(1, "четверть")
        elif x < 0 and y > 0:
            print(2, "четверть")
        elif x < 0 and y < 0:
            print(3, "четверть")
        elif x > 0 and y < 0:
            print(4, "четверть")
    else:
        print("Такой четверти не существует")

quarter()