# Определить, присутствует ли в заданном списке строк, некоторое число

def have_number (list_numbers, number):
    list = [j for j in list_numbers if str(number) in j]
    if len(list) == 0:
        print("Такого числа нет")
    else:
        print("Такое число есть")

have_number(['sdf5', 'asdf', '8', 'sdf23'], 13)