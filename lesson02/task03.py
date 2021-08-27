"""
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def get_name(self):
        return self._name

    @property
    def get_price(self):
        return self._price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.get_name, self.get_price)


if __name__ == '__main__':
    idr_A = ItemDiscountReport('item1', '2000')
    idr_A.get_parent_data()
