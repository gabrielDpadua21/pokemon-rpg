from random import choice
NAMES = ['Brok', 'Misty', 'Gary', 'John']

class Person:

    def __init__(self, name=None, pokemons=[]) -> None:
        self.name = name if name else choice(NAMES)
        self.pokemons = pokemons

    def catch(self, pokemon) -> None:
        self.pokemons.append(pokemon)
        print(f"{self.name} catch {pokemon.name} lvl {pokemon.level}")

    def __str__(self) -> str:
        return f"Name: {self.name}"
    
    def pokemons_list(self) -> None:
        if self.pokemons:
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("Not have pokemons")