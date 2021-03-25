#Длинная расширенная версия расчета 

Posetiteli_age = {}    #словарь для записи возраста посетителя
kol = int(input('Введите количество посетителей\n'))
cost = 0 #стоимость заказа
num_cost = 0 #кол-во заказов со стоимостью - скидку 10% можно получить при регистрации только 3-х ПЛАТНЫХ заказов
discont = 1 #коэффициент скидки на весь заказ
less_18yo = []
more_25yo = []
ot18_do25 = []
text = 'Полная стоимость заказа составляет '

for i in range(1, kol+1):
    Posetiteli_age[i] = int(input(f"Введите возраст посетителя №{i}: "))
    if Posetiteli_age[i] < 0:
        print (f'Ошибка! Возраст не может быть меньше 0, посетитель №{i} не будет учтен в расчете')
        continue
    elif Posetiteli_age[i] > 25:
        cost += 1390
        num_cost += 1
        more_25yo.append (i)
    elif 18 <= Posetiteli_age[i] <= 25:    
        cost += 990
        num_cost += 1
        ot18_do25.append (i)
    else:
        less_18yo.append(i)

print()       
if more_25yo:
    print ('Будут оформлены билеты по 1390 рублей (категория старше 25 лет):')
    for i in more_25yo:
        print (f'Посетитель №{i} (возраст {Posetiteli_age[i]})' )

if ot18_do25:
    print ('Будут оформлены билеты по 990 рублей (категория старше 18 и до 25 лет):')
    for i in ot18_do25:
        print (f'Посетитель №{i} (возраст {Posetiteli_age[i]})' )

if less_18yo:
    print ('Следующим посетителям будут оформлены бесплатные билеты (категория до 18 лет):')
    for i in less_18yo:
        print (f'Посетитель №{i} (возраст {Posetiteli_age[i]})' )

if num_cost >= 3:
        print ('Вы получили скидку 10% на всю сумму заказа!')
        text = 'Полная стоимость заказа с учетом скидки составляет'
        discont = 0.9

print()
print(f'{text} {round (cost * discont)} руб')
