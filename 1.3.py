import re
print('Варіант №24, Лaбораторна робота №1, Завдання #2:знайти значення функції')
"""
обраховує значення певної функції під номером 24
"""
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
def f():
    global x
    type_float()
    if x <= 13:
        y = -1 / (x**2 + 9)
    else :
        y = -(x**2 + 9)
    print('значення функції = ' + str(round(100*y)/100))
f()