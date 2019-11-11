import re
print('Варіант №24, Лaбораторна робота №1, Завдання #1')
ind = 0
num = ('першої','другої','третьої')
def type_float():
    global x
    global ind
    x= input('введіть правильне значення ' + str(num[ind]) + ' змінної опору  \n')
    ident = bool(re.match('\s{0,}[-+]?[0-9]*\.?[0-9]*\s{0,}$',x))
    if x == '':
        type_float()
    else:
        if ident == True:
            ind+=1
            x= float(x)
            return x
        else:
            type_float()
def resist_3() :
     global x
     type_float()
     res1 = x
     type_float()
     res2 = x
     type_float()
     res3 = x
     fin = (res1 * res2 * res3) / (res1 * res2 + res2 * res3 + res3 * res1)
     print('результуючий опір = ' + str(round(100*(fin))/100))
resist_3()
