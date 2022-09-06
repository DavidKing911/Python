import random

def shuffle():
    lst = list(range(1, 15))
    print(f"Изначальный список -> {lst}")
    random.shuffle(lst)
    print(f"Перемешанный список -> {lst}")

shuffle()