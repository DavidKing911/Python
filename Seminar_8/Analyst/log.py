from datetime import datetime as dt

def logger(choice, result):
    """
    Записывает время операции, саму операцию и её результат
    """
    time = dt.now().strftime('%m.%d.%Y - %H:%M')
    with open('Seminar_8/Analyst/log.csv', 'a', encoding = 'UTF-8') as file:
        file.write(f'{time}: {choice} - {result}\n')