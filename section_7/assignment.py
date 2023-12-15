# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if isinstance(new_price, float) and new_price >= 10:
            self._price = new_price
        else:
            print('Invalid price')

    price = property(get_price, set_price)

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if new_size in ('small', 'medium', 'large'):
            self._size = new_size
        else:
            print('Wrong definition of size')

    size = property(get_size, set_size)

    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand in ('LoLo', 'Digi', 'Kara'):
            self._brand = new_brand
        else:
            print('Wrong definition of brand')


class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and new_price >= 10:
            self._price = new_price
        else:
            print('Invalid price')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size in ('small', 'medium', 'large'):
            self._size = new_size
        else:
            print('Wrong definition of size')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand in ('LoLo', 'Digi', 'Kara'):
            self._brand = new_brand
        else:
            print('Wrong definition of brand')
