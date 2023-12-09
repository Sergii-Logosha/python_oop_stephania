# 09.12.23. Sergii Logosha sergiilogosha@gmail.com

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year


car = Car("Ford", 'F150', 2023)
print(car.brand)
print(car._year)
