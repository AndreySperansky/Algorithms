"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Постарайтесь решить задачу двумя способами:
1. Через цикл
Вариант исполнения: в бесконечном цикле запрашивайте вид операции, например, +, - или *
Проверяйте вид операции и запускайте соответствующую команду
Предусмотрите выход из бесконечного цикла
2. Рекурсией.
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def calc():
    """Recursion"""
    oper_type = input('Введите операцию (+, -, *, /) или 0 для выхода:')
    
    if oper_type == '0':
        return "Выход"
    
    else:
        if oper_type in "+-*/":
            try:
                num_1 = int(input("Введите первое число: "))
                num_2 = int(input("Введите второе число: "))
                
                if oper_type == '+':
                    res = num_1 + num_2
                    print(f'Ваш результат {res}')
                    return calc()  # это рекурсивный вызов функции
                
                elif oper_type == '-':
                    res = num_1 - num_2
                    print(f'Ваш результат {res}')
                    return calc()  # это рекурсивный вызов функции
                
                elif oper_type == '*':
                    res = num_1 * num_2
                    print(f'Ваш результат {res}')
                    return calc()  # это рекурсивный вызов функции
                
                elif oper_type == '/':
                    if num_2 != 0:
                        res = num_1 / num_2
                        print(f'Ваш результат {res}')
                        return calc()  # это рекурсивный вызов функции
                    else:
                        print("Деление на 0 невозможно")
                    return calc()  # это рекурсивный вызов функции
            
            
            except ValueError:
                print("Вы ввели строку вместо числа")
        
        else:
            print("Введен неверный символ")
            return calc()  # это рекурсивный вызов функции

