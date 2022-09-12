# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

list_number = [get_number("Введите число: ") for i in range(get_number("Введите размер списка: "))]
list_number_2 = []

def fill_list_num_2(list_num, list_num_2):
    for i in range(len(list_num)):
        count = 0
        for j in range(len(list_num)):
            if list_num[i] == list_num[j]:
                count += 1
        if count == 1:
            list_num_2.append(list_num[i])
    return list_num_2

print(f"Исходная последовательность -> {list_number}")
print(f"Список неповторяющихся элементов исходной последовательности -> {fill_list_num_2(list_number, list_number_2)}")