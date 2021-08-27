"""
3. Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
from random import random, randrange


rnd_list = []
rnd_dict = {}


def gen_rnd(a, b):
    rnd = randrange(a, b)
    rnd_list.append(rnd)
    rnd_dict[f'elem_{len(rnd_list)-1}'] = rnd


if __name__ == '__main__':
    for _ in range(10):
        gen_rnd(2, 55)
    print(rnd_list, rnd_dict, sep='\n')
