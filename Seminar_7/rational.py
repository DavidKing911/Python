# Калькулятор рациональных чисел

x = 0
y = 0

def init(a,b):
    global x
    global y
    x = float(a)
    y = float(b)

def sum():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def div():
    return x / y