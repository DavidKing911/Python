# Найти произведение пар чисел в списке. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
list_numbers = [2, 3, 5, 7, 4, 7]
list_numbers_2 = []

def composition(list_num, list_num_2):
    list_num_2 = ([list_num[i] * list_num[len(list_num) - i - 1] for i in range(int(len(list_num)/2 + len(list_num) % 2))])
    return list_num_2

print(f"Произведение пар чисел списка -> {composition(list_numbers, list_numbers_2)}")