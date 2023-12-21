# 17.12.23. Sergii Logosha sergiilogosha@gmail.com

class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('Please, provide a correct type for item')

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print('This item is not in the backpack')
            return 0

    def has_item(self, item):
        return item in self._items


my_backpack = Backpack()
print(my_backpack.items)

my_backpack.add_items('Water Bottle')
print(my_backpack.items)

my_backpack.add_items('Sleeping Bag')
print(my_backpack.items)

has_water_bottle = my_backpack.has_item('Water Bottle')
print(has_water_bottle)

my_backpack.remove_item('Water Bottle')
print(my_backpack.items)

my_backpack.remove_item('Sleeping Bag')
print(my_backpack.items)

my_backpack.remove_item('Apple')
print(my_backpack.items)
