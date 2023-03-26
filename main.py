from eletric_pokemon import EletricPokemon
from fire_pokemon import FirePokemon
from water_pokemon import WaterPokemon
from wind_pokemon import WindPokemon
from player import Player


if __name__ == '__main__':
    print('Pokemon RPG')
    player_name = input('Type your name: ')
    player = Player(player_name)
    my_pokemon = EletricPokemon('Pikachu')
    new_pokemon = FirePokemon('Charmander')

    player.add_pokemons(my_pokemon)
    player.add_pokemons(new_pokemon)

    print(player)
    player.pokemons_list()