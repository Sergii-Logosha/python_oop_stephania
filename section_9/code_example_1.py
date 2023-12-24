# 23.12.23. Sergii Logosha sergiilogosha@gmail.com

class Vehicle:
    def __init__(self, color, license_plate, is_electric):
        self.color = color
        self.license_plate = license_plate
        self.is_electric = is_electric

    def print_license_plate(self):
        print(self.license_plate)

    def show_info(self):
        print('My vehicle:')
        print(f'Color: {self.color}')
        print(f'License plate: {self.license_plate}')
        print(f'Is electric: {self.is_electric}')


class Employee:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def show_vehicle_info(self):
        self.vehicle.show_info()


kia = Vehicle('Grey', 'AX8181HK', is_electric=False)
sergii = Employee('Sergii', kia)

sergii.show_vehicle_info()
