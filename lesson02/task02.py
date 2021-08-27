"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.name, self.price)


if __name__ == '__main__':
    idr_A = ItemDiscountReport('item1', '2000')
    idr_A.get_parent_data()
