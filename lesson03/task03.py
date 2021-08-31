"""
3. Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""


def dict_create(keys_list, values_list):
    result = {}
    for i in range(len(keys_list)):
        key = keys_list[i]
        value = None
        if i < len(values_list):
            value = values_list[i]
        result[key] = value
    return result


if __name__ == '__main__':
    keys = ['A', 'B', 'C', 'D']
    values = [32, 43, 8]
    dict_result = dict_create(keys, values)
    print(dict_result)

    keys = ['A', 'B']
    values = [32, 43, 8]
    dict_result = dict_create(keys, values)
    print(dict_result)
