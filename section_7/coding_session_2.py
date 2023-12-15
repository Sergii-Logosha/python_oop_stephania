# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print('Invalid value for radius parameter')


blue_circle = Circle(10.0)
print(blue_circle.get_radius())
blue_circle.set_radius(5.0)
print(blue_circle.get_radius())
