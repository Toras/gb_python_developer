"""
2. Дополнить следующую функцию недостающим кодом:

def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import pathlib


def custom_key(f):
    return not f.is_dir()


def print_directory_contents(s_path, level):
    start_dir = pathlib.Path(s_path)
    print('-'*level + ' ' + start_dir.name)
    if start_dir.is_dir():
        files = [file for file in start_dir.iterdir()]
        files.sort(key=custom_key)
        for f_c in files:
            print_directory_contents(f_c, level+1)


if __name__ == '__main__':
    print_directory_contents('D:\#distrib\!Internet', 0)
