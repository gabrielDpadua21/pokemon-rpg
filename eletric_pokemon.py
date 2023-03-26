from pokemon import Pokemon

class EletricPokemon(Pokemon):
    element = 'Eletric'

    def __init__(self, species, level=1, name=None):
        self.species = species
        self.level = level
        self.name = name if name else species
    
    def attack(self, target) -> str:
        return f"{self.name} use thunder shock on {target.name}"