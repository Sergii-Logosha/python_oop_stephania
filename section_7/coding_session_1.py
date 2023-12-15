# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class Backpack:

    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Error: new_items must be a list")


my_backpack = Backpack()
print(my_backpack.get_items())
my_backpack.set_items(['Watter Bottle', 'First Aid Kit', 'Sleeping Bag'])
print(my_backpack.get_items())
