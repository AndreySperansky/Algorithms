"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

ODD = 0
EVEN = 0

try:
	NUM = int(input('Введите число: '))
	TMP = NUM
	while TMP > 0:
		if TMP % 10 % 2 == 0:
			EVEN += 1
		else:
			ODD += 1
		TMP = TMP // 10
	
	print(f'Число {NUM} содержит {EVEN} четных числа и {ODD} нечетных числа')
except ValueError:
	print('Ошибка, нужно ввести целое число!')
