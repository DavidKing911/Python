import complex as compl
import rational as ratio
import ui
import logs


def msg_compl(first_r, first_mn, second_r, second_mn, sign):
    '''
    Функция получает данные и формирует строку из них
    '''
    if first_mn >= 0:
        data_log = '(' + str(first_r) + ' + ' + str(first_mn)+ 'j' + ')' + ' ' + sign + ' ' + '(' + str(second_r)
    elif first_mn < 0:
        data_log = '(' + str(first_r) + ' + (' + str(first_mn)+ 'j)' + ')' + ' ' + sign + ' ' + '(' + str(second_r)
    if second_mn >= 0:
        data_log = data_log + ' + ' + str(second_mn) + 'j' + ')'
    if second_mn < 0:
        data_log = data_log  + ' + (' + str(second_mn) + 'j)' + ')'
    return data_log  
             
def button_click():
    '''
    Функция запрашивает данные, решает и выводит
    '''
    name=ui.choice_calc('Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2: ')
    if name==1:
        first_r=ui.rational_number('Введите первое рациональное число: ')  
        second_r=ui.rational_number('Введите второе рациональное число: ') 
        sign=ui.operation('Введите знак операции: (+, -, *, /): ')
        ratio.init(first_r, second_r)
        if sign == '+':
            result=ratio.sum()
        if sign == '-':
            result=ratio.sub()
        if sign == '*':
            result=ratio.mult()
        if sign == '/':
            if second_r==0:
                print('Деление на 0 невозможно!')
                data_log = '' + str(first_r) + ' '+ sign+ ' ' + str(second_r)
                logs.logger(data_log, "Деление на 0 невозможно!")
                exit()
            else:
                result=ratio.div()
        data_log = '' + str(first_r) + ' '+ sign+ ' ' + str(second_r)
        print(f"Для этого примера: {data_log} ответ будет: {result}")  
        logs.logger(data_log, result)
    elif name==2:
        first_r=ui.complex_number('Введите действительную часть первого числа: ') 
        first_mn=ui.complex_number('Введите мнимую часть первого числа: ') 
        second_r=ui.complex_number('Введите действительную часть второго числа: ') 
        second_mn=ui.complex_number('Введите мнимую часть второго числа: ') 
        
        sign=ui.operation('Введите знак операции: (+, -, *, /): ')
        compl.init(first_r, first_mn, second_r, second_mn)
        if sign == '+':
            result=compl.sum()
        if sign == '-':
            result=compl.sub()
        if sign == '*':
            result=compl.mult()
        if sign == '/':
            if second_r==0 and second_mn==0:
                print('Деление на 0 невозможно!')
                data_log=msg_compl(first_r, first_mn, second_r, second_mn, sign)               
                logs.logger(data_log, "Деление на 0 невозможно!")
                exit()
            else:
                result=compl.div()
        
        data_log=msg_compl(first_r, first_mn, second_r, second_mn, sign)               
        print(f"Для этого примера: {data_log} ответ будет: {result}")          
        logs.logger(data_log, result)