# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = 5
print(list((-3) ** x for x in range(n)))