print(" Программа расчета дохода по депозитам ")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# заданные значения процентов по депозитам в банках
money=float(input('Введите сумму вклада (руб): '))
pc=list(per_cent.values())
# список процентных ставок
banki=list(per_cent.keys())
deposit=pc.copy()
for i in range(len(pc)):
    deposit[i]*=money
    #получаем список с прибылью вкладов
print('Доходность вклада: ')
for i in range(len(deposit)):
    print("  в банке ", banki[i], "(процентная ставка ", pc[i], ") -", round(deposit[i],2), "руб")
    # выводим подробно инфо о прибыли и ставках по банкам
# print(deposit)
# так надо было написать в задании - просто вывести список
print("Максимальная сумма, которую Вы можете заработать -", 
        round(max(deposit),2), "руб, в банке", banki[deposit.index(max(deposit))])