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

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)


my_backpack = Backpack()
my_backpack.add_items('Water Bottle')
my_backpack.add_items('Sleeping Bag')
my_backpack.add_items('Candy')

print(f'Unsorted list:')
my_backpack.show_items()
print(f'Sorted list:')
my_backpack.show_items(True)
