from eletric_pokemon import EletricPokemon
from fire_pokemon import FirePokemon
from water_pokemon import WaterPokemon
from wind_pokemon import WindPokemon
from player import Player
from enemy import Enemy

first_catch = {
    "1": WindPokemon("Bulbassauro", 1),
    "2": FirePokemon("Charmarder", 1),
    "3": WaterPokemon("Squardle", 1)
}

def init_game(player):
    print("Choose your first Pokemon: ")
    print("1 - Bulbassauro - lvl 1")
    print("2 - Charmarder - lvl 1")
    print("3 - Squardle - lvl 1")
    while True:
        try:
            option = input("Type the pokemon choose: ")
            first_pokemon = first_catch[option]
            player.catch(first_pokemon)
            break
        except:
            print("Wrong option, try again!!!")


if __name__ == '__main__':
    print('Pokemon RPG')
    player_name = input('Type your name: ')
    player = Player(player_name)
    init_game(player)
    enemy = Enemy()
    print(player)
    player.pokemons_list()
    print(enemy)
    enemy.pokemons_list()