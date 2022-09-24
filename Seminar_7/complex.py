# Калькулятор комплексных чисел
# ad, bd - действительные части
# am, bm - мнимые части

x = 0
y = 0

def init(ad, am, bd, bm):
    global x
    global y
    x = complex(ad, am)
    y = complex(bd, bm)

def sum():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def div():
    return x / y