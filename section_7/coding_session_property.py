# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        print('Calling the getter...')
        return self._items

    @items.setter
    def items(self, new_list_of_items):
        print('Calling the setter...')
        if isinstance(new_list_of_items, list):
            self._items = new_list_of_items
        else:
            print('Item is not a list')


my_backpack = Backpack()
print(my_backpack.items)
my_backpack.items = ['watter Bottle', 'Rope']
print(my_backpack.items)
