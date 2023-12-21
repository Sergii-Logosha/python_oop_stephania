# 17.12.23. Sergii Logosha sergiilogosha@gmail.com

class Circle:

    pi = 3.1416

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # Define your method below:
    def find_area(self):
        return Circle.pi * self.radius ** 2


blue_circle = Circle(15, "Blue")

# Write your code below:
area = blue_circle.find_area()
print(area)