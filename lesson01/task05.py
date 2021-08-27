"""
5. Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция —
общую сумму по вкладу на конец периода.
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


def calc_deposit(dep_sum, dep_period, dep_add_sum=0):
    def calc_add_rate(period, rate, add_sum, cur_period):
        add_result = 0
        if cur_period in range(1, period-1):
            add_result = add_sum + add_sum * rate / 100 / 12
        return add_result

    dep_rate = get_rate(dep_sum, dep_period)

    result = dep_sum
    if dep_rate:
        for i in range(dep_period):
            rate_sum = result * dep_rate / 100 / 12
            result += rate_sum
            if dep_add_sum != 0:
                result += calc_add_rate(dep_period, dep_rate, dep_add_sum, i)
    else:
        return None

    return result


if __name__ == '__main__':
    end_sum = calc_deposit(int(input('Введите сумму: ')), int(input('Введите срок: ')),
                           int(input('Введите сумму ежемесячного взноса: ')))
    print(end_sum if end_sum else '')
