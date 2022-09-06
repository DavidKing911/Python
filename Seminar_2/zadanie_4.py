# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

num = int(input("Введите число: "))

def fill_array(n):
    array1 = []
    for i in range(n):
        array1.append(randint(-n, n + 1))
    return array1

def comp_element(array1, n):
    file = open("Seminar_2/file.txt")
    array2 = []
    comp = 1
    print(f"Список из {n} элементов, заполненых числами из промежутка [{-n}, {n}] -> {array1}")
    for i in file.read():
        if i.isdigit():
            i = int(i)
            if 0 <= i <= n - 1:
                array2.append(i)
                comp *= array1[i]
    file.close()
    print(f"Произведение элементов на позициях {array2} -> {comp}")

array = fill_array(num)
comp_element(array, num)