# Найти сумму чисел списка стоящих на нечетной позиции
list_numbers = [2, 3, 5, 9, 3, 5]
amount = [list_numbers[i] for i in range(1, len(list_numbers), 2)]
print(f'Сумма элементов, стоящих на нечётной позициях -> {sum(amount)}')