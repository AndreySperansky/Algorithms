"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


SUM = 0
ITEM = 1

try:
	NUM = int(input('Введите число: '))
	while NUM > 0:
		print(ITEM, end = ' ')
		SUM = SUM + ITEM
		ITEM = ITEM / (-2)
		NUM = NUM - 1
	print('\n', f'Сумма последовательности равна: {SUM}')
except ValueError:
	print('Ошибка, нужно ввести целое число!')
	
