# 17.12.23. Sergii Logosha sergiilogosha@gmail.com

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        return self.radius * 2


circle = Circle(5)
diameter = circle.get_diameter()
print(diameter)