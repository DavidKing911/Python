import csv
import view as v

def write_cvs():
    '''
    Запись в csv фаил
    '''
    lst = []
    text = v.get_action('Фамилия Имя: ')
    lst.append(text)
    text = v.get_action('Номер телефона: ')
    lst.append(text)
    text = v.get_action('Комментарий: ')
    lst.append(text)
    with open ('Seminar_7/Analyst/phone_book.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=' ', lineterminator='\r')
        file_writer.writerow(lst)