"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в
дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна
передаваться переменная — скидка), и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
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
    def __init__(self, discount, *args):
        self._discount = discount
        super(ItemDiscountReport, self).__init__(*args)

    def get_parent_data(self):
        print(self.get_name, self.price)

    def __str__(self):
        return str(self.price - self.price * self._discount / 100)


if __name__ == '__main__':
    idr_A = ItemDiscountReport(4, 'item1', 2000)
    idr_A.get_parent_data()
    print(idr_A)
