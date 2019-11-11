import math
import re
"""
Ввести три додатних числа а, b, с. Перевірити, чи будуть вони сторонами трикутника. Якщо так, то обчислити площу цього трикутника.
"""
print('Варіант №24, Лaбораторна робота №1,Завдання #2')
num=('першої', 'другої', 'третьої')
ind=0
def type_float():
    global x
    global ind
    x= input('введіть значення ' + str(num[ind]) + ' сторони  \n')
    ident = bool(re.match('\s{0,}[+]?[0-9]*\.?[0-9]*\s{0,}$',x))
    if x == '':
        type_float()
    else:
        if ident == True:
            ind+=1
            x= float(x)
            return x
        else:
            type_float()
def triangle():
    global x
    type_float()
    a = x
    type_float()
    b = x
    type_float()
    c = x
    if a < (b+c) and b < (c+a) and c < (a+b) :
       print('Такий трикутник існує')
       v = (a+b+c)/2
       f = math.sqrt((v*(v-a)*(v-b)*(v-c)))
       print('Площа трикутника = ' + str(f))
    else:
        print('такого трикутника не існує')
triangle()