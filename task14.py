""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. """

#-----------------------------------------------------------------
numberTask14 = abs(int(input('Введите число: ')))
stop = 0
num = 2
for i in range(numberTask14):
    if stop != 1:
        num = num ** i
        if num <= numberTask14:
            print(num, end=' ')
            num = 2
        else:
            stop = 1
    else:
        i = numberTask14