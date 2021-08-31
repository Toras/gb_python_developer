"""
6. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReportName(ItemDiscount):
    def __init__(self, discount=0, *args):
        self._discount = discount
        super(ItemDiscountReportName, self).__init__(*args)

    def get_parent_data(self):
        print(self.get_name)


class ItemDiscountReportPrice(ItemDiscount):
    def __init__(self, discount=0, *args):
        self._discount = discount
        super(ItemDiscountReportPrice, self).__init__(*args)

    def get_parent_data(self):
        print(self.price)


def class_obj_handler(class_obj):
    class_obj.get_parent_data()


if __name__ == '__main__':
    idr_A = ItemDiscountReportName(4, 'item1', 2000)
    idr_B = ItemDiscountReportPrice(4, 'item1', 2000)

    idr_A.get_parent_data()
    idr_B.get_parent_data()

    for i in (idr_A, idr_B):
        i.get_parent_data()

    class_obj_handler(idr_A)
    class_obj_handler(idr_B)
