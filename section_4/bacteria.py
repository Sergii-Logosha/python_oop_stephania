# 26.11.23. Sergii Logosha sergiilogosha@gmail.com

class Bacterium:

    def __init__(self, species, shape, is_poisonous, x, y, protection_level=2,):
        self.species = species
        self.shape = shape
        self.is_poisonous = is_poisonous
        self.protection_level = protection_level
        self.number_of_lives = 10
        self.x = x
        self.y = y


helicobacter = Bacterium('Helicobacter Pylori', 'helix', False, 7, 45, 15)
staphylococcus = Bacterium('Staphylococcus', 'spherical', True, 5, 50, 29)
salmonella = Bacterium('Salmonella', 'cylindrical', True, 10, 0, 0)
