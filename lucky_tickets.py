#подсчет кол-ва счастливых билетов
lucky_counter = 0
lucky_counter1 = 0
for i in range (0, 999999+1): # можно не от 0 а от 1000 начинать - так даже правильней, т.к. не засчитает билетик 000 000
    ticket = str(i).rjust(6, '0')
    right_part = ticket[:3]
    left_part = ticket[3:]
    sumRP = 0
    sumLP = 0
    
    for elem in right_part:
        sumRP = sumRP + int(elem)
    
    for elem in left_part:
        sumLP = sumLP + int(elem)
    
    if sumLP == sumRP:
        lucky_counter +=1
    
    right_part1 = [int(ticket[i]) for i in range(0, len(ticket) // 2)]
    left_part1 = [int(ticket[i]) for i in range(len(ticket) // 2, len(ticket))]   
 
    if sum(right_part1) == sum(left_part1):
       lucky_counter1 += 1

    
print(lucky_counter) #способ прямого задания длины и перевода строки в инт поэлементно

print(lucky_counter1) #способ получения через генератор инт (генератором разбивает и преобразует в инт полученную строку тикета)