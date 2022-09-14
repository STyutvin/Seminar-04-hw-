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

# Задача №4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):
    with open('file04.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,101)

def create_polynom(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    wrt = ''
    if len(lst) < 1:
        wrt = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wrt += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wrt += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wrt += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wrt += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wrt += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wrt += ' = 0'
    return wrt

k = int(input("Введите натуральную степень k = "))
cfc = create_polynom(k)
write_file(create_str(cfc))