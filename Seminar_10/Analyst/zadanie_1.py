# Даны два списка чисел. Найдите все числа, которые входят как в первый, 
# так и во второй список и выведите их в порядке возрастания.
# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
print(list(set(i for i in [5, 3, 15, 6, 7, 2] if i in [5, 9, 2, 0, 1, 5, 7])))