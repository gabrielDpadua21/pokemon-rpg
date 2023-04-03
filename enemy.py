from random import choice
from person import Person
from pokemons_list import POKEMONS



class Enemy(Person):
    type = 'Enemy'

    def __init__(self, name=None, pokemons=[]):
        if not pokemons:
            for _ in range(2):
                pokemons.append(choice(POKEMONS))
        super().__init__(name=name, pokemons=pokemons)