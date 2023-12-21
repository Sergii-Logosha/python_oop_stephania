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

    def add_multiple_items(self, list_of_items):
        for item in list_of_items:
            self.add_items(item)

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
print(my_backpack.items)
my_backpack.add_multiple_items(['Watter Bottle, Sleeping Bag'])
print(my_backpack.items)
my_backpack.add_multiple_items(['Candy', 123, 'Knife'])
print(my_backpack.items)
