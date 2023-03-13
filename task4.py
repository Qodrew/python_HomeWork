"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
"""
# ---------------------------------------------------

while True:
    try:
        somethingNum = int(input('Введите целое положительно число: '))
        if isinstance(somethingNum, int) and somethingNum > 0:
            break
    except :
        print("Ошибка! Введено некорректное значение")

maxValueinNum = somethingNum % 10
while True:
    somethingNum = somethingNum // 10
    if somethingNum % 10 > maxValueinNum:
        maxValueinNum = somethingNum % 10
    elif somethingNum > 9:
        continue
    else:
        print(f'Максимальное число: {maxValueinNum}')
        break