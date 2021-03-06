"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

from random import randint


LST_LEN = 15
ARR = [randint(-99, 99) for i in range(LST_LEN)]
print(ARR)

MAX_EL = ARR[0]
MIN_EL = ARR[0]
MAX_IND = 0
MIN_IND = 0

for i in range(len(ARR)):
    if MAX_EL < ARR[i]:
        MAX_EL = ARR[i]
        MAX_IND = i
    if MIN_EL > ARR[i]:
        MIN_EL = ARR[i]
        MIN_IND = i
print(f'Максимальный элемент последовательности: {MAX_EL}, его индекс: {MAX_IND}')
print(f'Минимальный элемент последовательности: {MIN_EL}, eго индекс:  {MIN_IND}')

ARR[MIN_IND], ARR[MAX_IND] = MAX_EL, MIN_EL

print('Новая последовательность после замены: ')
print(ARR)
