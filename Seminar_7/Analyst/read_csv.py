import csv

def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('Seminar_7/Analyst/phone_book.csv', encoding='utf-8') as r_file:
        file_reader_1 = csv.reader(r_file, delimiter=' ')
        file_reader = []
        for line in file_reader_1:
            line = ' '.join(line)
            file_reader.append(line)
        return file_reader