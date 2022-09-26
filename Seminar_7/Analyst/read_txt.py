def read_txt():
    with open('Seminar_7/Analyst/phone_book.txt', 'r', encoding='utf-8') as file:
        file_reader_1 = file.readlines()
        file_reader = []
        for line in file_reader_1:
            line = line[:-2]
            file_reader.append(line)
    return file_reader