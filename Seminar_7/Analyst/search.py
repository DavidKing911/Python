import view as v

def search(lst_input: list)-> list:
    '''
    Поиск в телефонной книге
    '''
    text = v.get_action('Введите значение для поиска: ')
    line_output = []
    for line in lst_input:
        if text in line:
            line_output.append(line)
    return line_output