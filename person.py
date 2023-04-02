from random import choice, randint
NAMES = ['Brok', 'Misty', 'Gary', 'John']

class Person:
    pokemon_choose = None

    def __init__(self, name=None, pokemons=[]) -> None:
        self.name = name if name else choice(NAMES)
        self.pokemons = pokemons


    def __str__(self) -> str:
        return f"Name: {self.name}"


    def catch(self, pokemon) -> None:
        self.pokemons.append(pokemon)
        print(f"{self.name} catch {pokemon.name} lvl {pokemon.level}")


    def pokemons_list(self) -> None:
        if self.pokemons:
            for index, pokemon in enumerate(self.pokemons):
                print(f"{index + 1} - {pokemon}")
        else:
            print(f"{self.name} not have pokemons!!!")
    

    def choose(self) -> None:
        print('Choice a pokemon')
        self.pokemons_list()
        print('_____________________')
        while len(self.pokemons):
            try:
                option = int(input('Type the option: '))
                self.pokemon_choose = self.pokemons[(option - 1)]
                break
            except: 
                print('Wrong option, try again')
    
    
    def battle(self, enemy) -> None:
        print(f"PokeBattle {self.name} VS {enemy.name}")
        self.choose()
        print(f"{self.name} chooses: {self.pokemon_choose}")
        enemy_choice = choice(enemy.pokemons)
        print(f"{enemy.name} chooses: {enemy_choice}")
        print("BATTLE")
        print(self.pokemon_choose.attack(enemy_choice))
        print(enemy_choice.attack(self.pokemon_choose))
        winner = randint(1, 2)
        if winner == 1:
            print(f"{self.pokemon_choose.name} win battle - {self.name} is the winner")
        else:
            print(f"{enemy_choice.name} win battle - {enemy.name} is the winner")


