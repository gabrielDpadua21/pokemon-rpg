from eletric_pokemon import EletricPokemon
from fire_pokemon import FirePokemon
from water_pokemon import WaterPokemon
from wind_pokemon import WindPokemon
from player import Player
from enemy import Enemy
from banner import art

first_catch = {
    "1": WindPokemon("Bulbassauro", 1),
    "2": FirePokemon("Charmarder", 1),
    "3": WaterPokemon("Squardle", 1)
}

def init_game(player):
    print("------------------------------------------------------------------------------")
    print(f"Hello {player.name}, i am professor rocket!")
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
    print("Great now you are ready to start your jorney!")
    print("------------------------------------------------------------------------------")


def gameplay():
    pass


if __name__ == '__main__':
    print(art)
    print('Welcome to Pokemon RPG')
    player_name = input('Type your name: ')
    player = Player(player_name)
    init_game(player)
    print("Lets start: what do you want to do?")
    while True:
        print("------------------------------------------------------------------------------")
        print("1 - To explore")
        print("2 - Battle")
        print("3 - Pokemons list")
        print("4 - Player Status")
        print("0 - Exit")
        print("------------------------------------------------------------------------------")
        try:
            option = int(input("Type one option: "))
            if option < 1 or option > 4:
                print("Bye")
                break
            elif option == 1:
                player.to_explore()
            elif option == 2:
                enemy = Enemy()
                player.battle(enemy)
            elif option == 3:
                print("You pokemons list: ")
                player.pokemons_list()
            else:
                player.report()
        except:
            print("Wrong option, try again")

