"""
4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет
по нужной процентной ставке.
Функция возвращает сумму вклада на конец срока.
"""


def get_rate(dep_sum, dep_period):
    dep_dict_1 = {
        'begin_sum': 1000,
        'end_sum': 10000,
        6: 6,
        12: 7,
        24: 6.5
    }
    dep_dict_2 = {
        'begin_sum': 10000,
        'end_sum': 100000,
        6: 5,
        12: 6,
        24: 5
    }
    dep_dict_3 = {
        'begin_sum': 100000,
        'end_sum': 10000000,
        6: 7,
        12: 8,
        24: 7.5
    }
    try:
        if dep_sum in range(dep_dict_1['begin_sum'], dep_dict_1['end_sum']):
            dep_rate = dep_dict_1[dep_period]
        elif dep_sum in range(dep_dict_2['begin_sum'], dep_dict_2['end_sum']):
            dep_rate = dep_dict_2[dep_period]
        elif dep_sum in range(dep_dict_3['begin_sum'], dep_dict_3['end_sum']):
            dep_rate = dep_dict_3[dep_period]
        else:
            print(f'Нет подходящей ставки для суммы {dep_sum}')
            return None
    except KeyError:
        print(f'Нет подходящей ставки для периода {dep_period}')
        return None
    return dep_rate


def calc_deposit(dep_sum, dep_period):
    dep_rate = get_rate(dep_sum, dep_period)

    result = dep_sum
    if dep_rate:
        for _ in range(dep_period):
            rate_sum = result * dep_rate / 100 / 12
            result += rate_sum
    else:
        return None

    return result


if __name__ == '__main__':
    end_sum = calc_deposit(int(input('Введите сумму: ')), int(input('Введите срок: ')))
    print(end_sum if end_sum else '')
