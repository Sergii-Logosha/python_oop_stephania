# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class Circle:

    VALID_COLORS = ['Red', 'Green', 'Blue']

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print('Radius must be greater than 0')

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print('New color must be one of: Red, Green, Blue')

    color = property(get_color, set_color)


blue_circle = Circle(10, 'Blue')

print(blue_circle.radius)
blue_circle.radius = 16
print(blue_circle.radius)

print(blue_circle.color)
blue_circle.color = 'White'
print(blue_circle.color)
