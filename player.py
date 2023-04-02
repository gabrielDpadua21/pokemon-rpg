from random import choice, randint
from person import Person

class Player(Person):
    type = "player"

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