"""
1. Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену.
Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), отвечающую за
отображение информации о товаре в одной строке. Проверить работу программы, создав экземпляр (объект)
родительского класса.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.name, self.price)


if __name__ == '__main__':
    idr_A = ItemDiscountReport('item1', '2000')
    idr_A.get_parent_data()
