"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла
(без расширения).
"""
import os


def search_file(filename, dir_list):
    for dir_path, dir_names, file_names in os.walk(dir_list):
        for file_name in file_names:
            if file_name == filename:
                print(os.path.join(dir_path, file_name))
                print(os.path.splitext(file_name)[0])


if __name__ == '__main__':
    search_file('1.txt', '\\')
