
def exp_data():
    """
    Поиск и экспорт нужных данных
    """
    text = input("Введите значение для поиска: ")
    with open('Seminar_8/Analyst/data_bases.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
    for i in range(len(lst)):
        if text in lst[i]:
            temp = i % 6
            result = (lst[i-temp:i+5-temp])
            return text, result
    return text, ["Данные отсутсвуют"]