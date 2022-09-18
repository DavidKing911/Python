# Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.
import sympy as sm

def summa_polynomials():
    '''
    Считает сумму двух многочленов
    '''
    file_1 = open("Seminar_5/Programmer/file_1.txt")
    file_2 = open("Seminar_5/Programmer/file_2.txt")
    file_3 = open("Seminar_5/Programmer/file_3.txt", "w")
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