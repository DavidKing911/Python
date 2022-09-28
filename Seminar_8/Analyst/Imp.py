
def add(str):
    """
    Импорт данных
    """
    with open('Seminar_8/Analyst/data_bases.txt', 'a', encoding="utf-8") as f:
        f.write(str + '\n')