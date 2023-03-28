from random import randint

class Pokemon:
    
    def __init__(self, element, species, level=randint(1, 10), name=None):
        self.element = element
        self.species = species
        self.level = level
        self.name = name if name else species

    def __str__(self) -> str:
        return f"{self.name} / lvl {self.level} - {self.element}"
    
    def attack(self, target) -> str:
        return f"{self.name} attack {target.name}"
