import re
"""
програма обчислює певну суму, завдання №1 до другої лаби у методичці громової
"""

print('Варіант №25, Лaбораторна робота №1, Завдання #1')
s=0
def type_float():
    global x
    x= input('введіть правильне значення змінної  \n')
    ident = bool(re.match('\s{0,}[-+]?[0-9]*\.?[0-9]*\s{0,}$',x))
    if x == '':
        type_float()
    else:
        if ident == True:
            x= float(x)
            return x
        else:
            type_float()
def type_float1():
    global x
    x= input('введіть правильне значення змінної  \n')
    ident = bool(re.match('\s{0,}[+]?[0-9]$',x))
    if x == '':
        type_float1()
    else:
        if ident == True:
            x= int(x)
            return x
        else:
            type_float1()
def summ():
    print('введіть значення змінної х')
    type_float()
    x1 = x
    print('введіть значення змінної n')
    type_float1()
    n = x
    for i in range(1,n+1):
        global s
        s+=((2 ** i) / (x1 - n))
    print('значення суми = 'str(round(s*100)/100))
summ()