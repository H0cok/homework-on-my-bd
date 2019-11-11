print('Варіант №25, Лaбораторна робота №2, Завдання #2')
import re
"""
Для чисел, що вводяться визначити відсоток додатнихі негативних чисел. При уведенні числа − 65432 закінчити роботу.
"""
k=[]
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
def numb():
    type_float()
    global k
    if x !=-65432:
        k.append(x)
        numb()
    else:
        return k
pos = 0
neg = 0
def prrrr():
    numb()
    global k
    global s
    global pos
    global neg
    if len(k) == 0:
        prrrr()
    for i in k:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
    print('відсоток додатніх ' + str(round(1000 * (pos / len(k))) / 10) + '% ' + 'відсоток від*ємних ' + str(
        round(1000 * (neg / len(k))) / 10) + '% ')
prrrr()