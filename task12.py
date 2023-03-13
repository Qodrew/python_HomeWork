"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа. """

#------------------------------------------------------------------------
firstNumber = abs(int(input('Введите первое натуральное число: ')))
secondNumber = abs(int(input('Введите второе натуральное число: ')))
sumOfNumbers = firstNumber + secondNumber
productOfNumbers = firstNumber * secondNumber
ansverFirstNum = int((sumOfNumbers - ((-sumOfNumbers) ** 2 - 4 * productOfNumbers) ** 0.5) / 2)
ansverSecondNum = int((sumOfNumbers + ((-sumOfNumbers) ** 2 - 4 * productOfNumbers) ** 0.5) / 2)
print(ansverFirstNum, ansverSecondNum)