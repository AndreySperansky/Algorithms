"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""

"""
Заполнение матрицы случайными числами
"""


ROW = int(input('Введите число строк матрицы: '))
CLMN = int(input('Введите число столбцов матрицы: '))
A = []

for i in range(ROW):
    b = []
    s = 0
    print(f"{i}-я строка:")
    for j in range(CLMN - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    A.append(b)

for i in A:
    print(i)
    
print('\n **************************************************************************************')
# Так покрасивше будет

for i in range(ROW):
    for j in range(CLMN):
        print("%3d" % A[i][j], end = '')
    print()
    