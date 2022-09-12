# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import sympy as sm

def summa_polynomials():
    '''
    Считает сумму двух многочленов
    '''
    x = sm.Symbol("x")
    file_1 = open("Seminar_4/file_1.txt")
    file_2 = open("Seminar_4/file_2.txt")
    file_3 = open("Seminar_4/file_3.txt", "w")
    a = file_1.read()
    b = file_2.read()
    polynom_1 = sm.parsing.sympy_parser.parse_expr(a)
    polynom_2 = sm.parsing.sympy_parser.parse_expr(b)
    sum_polynomials = polynom_1 + polynom_2
    file_3.write(str(sum_polynomials))
    file_1.close()
    file_2.close()
    file_3.close()

summa_polynomials()