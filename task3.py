"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
"""
# ---------------------------------------------------

while True:
    try:
        somethingNum = int(input('Введите целое положительно число: '))
        if isinstance(somethingNum, int) and somethingNum > 0:
            break
    except :
        print("Ошибка! Введено некорректное значение")

print(f'{somethingNum}{somethingNum*2}{somethingNum*3}')