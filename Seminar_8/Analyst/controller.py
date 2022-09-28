import Imp
import Inp
import Exp
import log

def button_click():
    number = Inp.choice()
    if number == 1:
        str_1, str_2, str_3, str_4, str_5 = Inp.data()
        Imp.add(str_1)
        Imp.add(str_2)
        Imp.add(str_3)
        Imp.add(str_4)
        Imp.add(str_5)
        Imp.add('')
        log.logger('Импорт', (str_1, str_2, str_3, str_4, str_5))
    elif number == 2:
        text = Exp.exp_data()
        print(text)
        log.logger('Экспорт', (text))
    else:
        print("Вы ввели неверное значение")