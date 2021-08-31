"""
2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


if __name__ == '__main__':
    val = input('Введите число: ')
    val = ''.join(['.' if ch == ',' else ch for ch in val])
    try:
        val = int(val)
        print('Целое')
    except ValueError:
        try:
            val = float(val)
            print('Дробное')
            pos = str(val).find('.')
            val1, val2 = int(str(val)[:pos]), int(str(val)[pos+1:])
            if val1 == val2:
                print(True)
            else:
                print(False)
        except ValueError:
            print('Не число')
