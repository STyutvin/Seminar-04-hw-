# Задача №1. Вычислить число c заданной точностью d.
# from math import pi
# d =  int(input('Введите число для заданной точности числа Пи: '))
# print(f'Число Пи с заданной точностью {d} равно {round(pi, d)}')
#-------------------------------------------------

# Задача №2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n=int(input('Введите число N: '))
# empty_list=[]
# for i in range(0,n-1):
#     if n%(n-i)==0:
#         empty_list.append((int(n/(n-i))))
# print(f'Список простых множителей для числа N={n}: {empty_list}')
#-------------------------------------------------

# Задача №3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# from random import randint
# some_list = []
# i = 1
# n = int(input('Введите количество элементов в списке: '))
# for i in range(n):
#     some_list.append(randint(1,5))
#     i += 1
# print(f'Ваш случайно сгенерированный список из {n} элементов: {some_list}')
# unique_list=list(set(some_list))
# print(f'Список уникальных элементов {unique_list}')
#-------------------------------------------------