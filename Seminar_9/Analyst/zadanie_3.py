# Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать 
# словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут 
# типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. 
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. 
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
string = '23334579234562047'

def count_it(sequence):
    new_dict = {}
    my_dict = {int(i): sequence.count(i) for i in sequence}
    sorted_keys = sorted(my_dict, key=my_dict.get)
    for i in sorted_keys:
        new_dict[i] = my_dict[i]
    return dict(list(new_dict.items())[-3:])

print(count_it(string))