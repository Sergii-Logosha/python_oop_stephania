# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class Dog:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print('Please, enter a valid name')


my_dog = Dog("Joy", 3)
print(my_dog.get_name())
my_dog.set_name('Figma')
print(my_dog.get_name())
