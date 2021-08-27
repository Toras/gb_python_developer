"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод
родительского класса и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной
строке).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def get_name(self):
        return self._name


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.get_name, self.price)


if __name__ == '__main__':
    idr_A = ItemDiscountReport('item1', '2000')
    idr_A.get_parent_data()
    idr_A.price = 100
    print(idr_A.price)
    idr_A.get_parent_data()
