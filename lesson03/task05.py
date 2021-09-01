"""
5. Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения,
вывод всех вхождений.
Реализовать замену всех найденных подстрок на новое значение
и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""
import os
import fileinput
import re


def create_and_open(filename):
    if os.path.exists(filename):
        print('файл существует')
    with open(filename, mode='w') as filewrite:
        list1 = [f'example{i}' for i in range(65, 91)]
        list2 = [i for i in range(65, 91)]
        list3 = zip(list1, list2)
        for el in list3:
            filewrite.writelines(f'{el[0]}: {el[1]}\n')
    read_and_print(filename)


def read_and_print(filename):
    with open(filename, mode='r') as fileread:
        list1 = fileread.read()
        list1 = list1.split(sep='\n')
        print(*list1, sep='\n')


def find_equals(search_str, search_place, find_all=False):
    result = []
    with open(search_place, mode='r') as fileread:
        for line in fileread:
            if search_str in line:
                if not find_all:
                    return line.split(sep='\n')[0]
                else:
                    result.append(line.split(sep='\n')[0])
    return result


def find_and_replace(search_str, replace_str, search_place, replace_all=False):
    with fileinput.FileInput(search_place, inplace=True) as filesearch:
        found = False
        for line in filesearch:
            if search_str in line:
                if not replace_all and not found:
                    print(line.replace(search_str, replace_str), end='')
                    found = True
                elif replace_all:
                    print(line.replace(search_str, replace_str), end='')
                else:
                    print(line, end='')
            else:
                print(line, end='')


def find_strings(regexp, search_place):
    result = []

    with open(search_place, 'r') as filesearch:
        for line in filesearch:
            line = line.split(sep='\n')[0]
            research = re.search(regexp, line)
            if research is not None:
                result.append(research)

    return result


if __name__ == '__main__':
    file = '2.txt'
    create_and_open(file)
    print(find_equals('e8', file))
    print(find_equals('e8', file, True))
    find_and_replace('e8', 'aaaaa', file, True)
    print(*find_strings(r'\s[0-9a-zA-z]*\s', file))
