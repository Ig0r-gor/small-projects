
def chis(a): # функция перевода строковых в числовой формат
    try:
        chislo = int(a)
    except ValueError as e:
        try:
            chislo = float(a)
        except ValueError as e:
            print('\nВведен неверный символ вместо числа. Повторите ввод')
            chislo = None
    return chislo

def bubblig(array): # функция сортировки массива
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def dva_poisk(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return right #останавливаем поиск

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент равен среднему,
        return (middle-1)  # возвращаем этот индекс-1
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return dva_poisk(array, element, left, middle - 1)
    else:  # иначе в правой
        return dva_poisk(array, element, middle + 1, right)

vyhod = True
while vyhod:

    # запрос на ввод значений для формирования списка
    LD=[1]
    while not (len(LD)-1):
        LD = input(' Введите через пробел несколько чисел.\n').split()
        if len(LD) < 2: next
        for i in range(len(LD)):
            cs = chis(LD[i])
            if cs is None:
                cs = chis(input(f'\nПовторите ввод числа вместо символа {LD[i]}:  '))
            LD[i]=cs
    print(LD)

    # запрос числа с которым будем сравнивать элементы списка
    obr = None
    while obr is None:
        while obr is None:
            obr = chis(input('\nВведите число для сравнения: '))
        if obr <= min(LD) or obr > max(LD):
            print(f'Данное число находится вне границ введенной последовательности\n {LD}, \nповторите ввод ')
            obr=None

    # сортировка списка LD, как понял пользоваться LD.sort() нельзя
    LD=bubblig(LD)

    indx=(dva_poisk(LD, obr, 0, LD.index(LD[-1])))
    print(indx)
    print(f'РЕШЕНИЕ: \nвведеное число {obr} больше {LD[indx]} с номером {indx+1} '
          f'и меньше или равно {LD[indx+1]} с номером {indx+2}')
    print(f'в введеной и отсортированной последовательности: ')
    print(', '.join(map(str, bubblig(LD))))
    print(f'справедливо неравенство {LD[indx]} < {obr} <= {LD[indx+1]}')

    vyhod = not ('+' == (input('\n введите "+" для выхода или начните сначала: ')))
