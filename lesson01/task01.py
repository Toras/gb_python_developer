"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции. Элементы строки (элементы таблицы умножения)
должны разделяться табуляцией.
"""


def mul_table(a, b):
    result = []
    for i in range(a):
        result.append([])
        for j in range(b):
            result[i].append((i+1) * (j+1))
        print('\t'.join([str(st) for st in result[i]]))


if __name__ == '__main__':
    mul_table(9, 9)
