# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 6782 -> 23    - 0,56 -> 11
number = float(input('Введите любое вещественное число: '))
f = str(number)
lst = f.split('.')
A = [int(x) for x in lst]
num1 = A[0]
num2 = A[1]
summ = 0
while num1 > 0:
    a = num1 % 10
    summ = summ + a
    num1 = num1 // 10
while num2 > 0:
    a = num2 % 10
    summ = summ + a
    num2 = num2 // 10
print(f'{number} -> Сумма цифр числа {summ}')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
number = int(input('Введите любое число: '))
lst = []
product = 1
print(f'Набор произведений чисел: ''[', end = (' '))
for i in range(1, number +1):
    # print((math.factorial(i)), end = (", "))
    product = product * i
    print(product, end = (', '))
print(']')

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}  # сумма 9.06
import math
number = int(input('Введите число: '))
dictionary = {i : round((1 + (1/i))**i,2) for i in range(1, number+1)}
print(f'Итоговая последовательность: {dictionary}')
summ=0
for i in range(1, number + 1):
    # print(dictionary[i])
    summ= summ+dictionary[i]
print(f'Cумма чисел последовательности: {summ}')

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
number = int(input("Введите число: "))
lst = [random.randint(-number, number) for i in range(number)]
print(f'Список из {number} элементов, заполненных числами из промежутка [{-number}, {number}]: {lst}')

with open('file.txt', 'w') as file:
    for i in range(number-1):
        a = random.randint(0, number-1)
        file.write(str(a) + '\n')
    file.write(str(a))
with open ('file.txt' , 'r') as f:
    a = f.read().split('\n')
b=[int(x) for x in a]
print(f'Случайные позиции: {b}')
     
product = 1
for i in range(0, len(b)):
    product = product * lst[b[i]]
print(f'Произведение элементов, находящихся на случайнных позициях: {product}')

# 5. Реализуйте алгоритм перемешивания списка.
import random
some_list = [1,2,3,4,5,6,7,8,9,10]
print(some_list)
random.shuffle(some_list)
print(some_list)
