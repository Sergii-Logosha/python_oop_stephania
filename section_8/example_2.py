# 17.12.23. Sergii Logosha sergiilogosha@gmail.com

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, increment=5):
        self.y += increment

    def move_down(self, increment=5):
        self.y -= increment

    def move_left(self, increment=5):
        self.x -= increment

    def move_right(self, increment=5):
        self.x += increment


warior = Player(10, 10)
print(warior.x, warior.y)
warior.move_up()
print(warior.x, warior.y)
