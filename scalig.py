# simple calc. Igor Gorbachev QAP33

operlist = ['+', '-', '*', '/'] #список функций

def mozhno():
    print ('\n Доступны функции: ')
    for i in operlist:
        print (i, end=' ')

def chis(a):
    try:
        chislo = int(a)
    except ValueError as e:
        try:
            chislo = float(a)
        except ValueError as e:
            print('\nВведен неверный символ вместо числа')
            chislo = None
    return chislo        

def dlina(b):
    if len(str(b)) > 12:
        print('\nКалькулятор простой,а Вы вводите слишком длинннннные числа!!!')
        chislo = None
    else:
        chislo = b
    
    return chislo

print (' Очень простой калькулятор.')

mozhno()
vyhod = True

while vyhod:
    x = None
    y = None
    while x is None:
        x = chis(input ('\nВведите первое число:  ') )
        x = dlina(x)
        
    oper = input('\n  Введите оператор: ')
    while oper not in operlist:
        print ('\nневерный оператор!')
        mozhno()
        oper = input('\nВведите оператор: ')    
        
    while y is None:
        y = chis(input ('\n Введите второе число:  '))
        y = dlina(y)
        
    while oper == '/' and not y:
        y = None
        print('\n на ноль делить нельзя!')
        while y is None:
            y = chis(input ('\n Введите второе число:  '))
            y = dlina(y)
            
    if oper == '/' :
            otvet = x / y
    elif oper == '+':
        otvet = x+y
    elif oper == '-':
        otvet = x-y
    elif oper == '*':
        otvet = x*y
    
    if x < 0:
        x =('(' + str(x) + ')')
    if y < 0:
        y =('(' + str(y) + ')')
    
    print('\n   Результат вычисления: ',x, oper, y, '=', round(otvet, 12))
    vyhod = not ('+' == (input ('\n введите "+" для выхода или продолжите вычисления:')))