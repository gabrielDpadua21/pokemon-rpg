from random import randint
from pokemon import Pokemon

class WindPokemon(Pokemon):
    element = 'Wind'

    def __init__(self, species, level=None, name=None):
        super().__init__(element=self.element, species=species, name=name)
    
    def attack(self, target) -> str:
        return f"{self.name} use Wind Spear on {target.name}"