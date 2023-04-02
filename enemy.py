from random import choice
from person import Person
from fire_pokemon import FirePokemon
from wind_pokemon import WindPokemon
from water_pokemon import WaterPokemon
from eletric_pokemon import EletricPokemon

POKEMONS = [
    FirePokemon("Charmilion"),
    WindPokemon("Bubassauro"),
    WaterPokemon("Squardle"),
    EletricPokemon("Raichu")
]

class Enemy(Person):
    type = 'Enemy'

    def __init__(self, name=None, pokemons=[]):
        if not pokemons:
            for _ in range(2):
                pokemons.append(choice(POKEMONS))
        super().__init__(name=name, pokemons=pokemons)