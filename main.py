from eletric_pokemon import EletricPokemon
from fire_pokemon import FirePokemon
from water_pokemon import WaterPokemon
from wind_pokemon import WindPokemon


if __name__ == '__main__':
    print('Pokemon RPG')
    my_pokemon = EletricPokemon('Pikachu')
    new_pokemon = FirePokemon('Charmander')

    print(my_pokemon)
    print(new_pokemon)