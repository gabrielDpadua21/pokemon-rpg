class Person:

    def __init__(self, name=None, pokemons=[]) -> None:
        self.name = name if name else 'Mistery'
        self.pokemons = pokemons

    def add_pokemons(self, pokemon) -> None:
        self.pokemons.append(pokemon)

    def __str__(self) -> str:
        return f"Name: {self.name}"
    
    def pokemons_list(self) -> None:
        for pokemon in self.pokemons:
            print(pokemon)