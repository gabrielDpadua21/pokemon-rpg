from eletric_pokemon import EletricPokemon
from fire_pokemon import FirePokemon
from water_pokemon import WaterPokemon
from wind_pokemon import WindPokemon
from player import Player
from enemy import Enemy


if __name__ == '__main__':
    print('Pokemon RPG')
    player_name = input('Type your name: ')
    player = Player(player_name)
    enemy = Enemy()
    my_pokemon = EletricPokemon('Pikachu')
    new_pokemon = FirePokemon('Charmander')

    print(player)
    player.pokemons_list()

    player.catch(my_pokemon)
    player.catch(new_pokemon)

    print(player)
    player.pokemons_list()
    print(enemy)