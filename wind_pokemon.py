from pokemon import Pokemon

class WindPokemon(Pokemon):
    element = 'Wind'

    def __init__(self, species, level=1, name=None):
        self.species = species
        self.level = level
        self.name = name if name else species
    
    def attack(self, target) -> str:
        return f"{self.name} use Wind Spear on {target.name}"