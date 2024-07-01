import random


class Boss:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        damage = random.randint(50, 150)
        player.take_damage(damage)
        print(f"{self.name} attacks you, dealing {damage} damage!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Congratulations! You have defeated the Gym Leader and won the game!")

    def show_stats(self):
        green = "\033[32m"
        yellow = "\033[33m"
        reset = "\033[0m"

        print(f"{green}Boss Stats{reset}".center(40, "="))
        print(f"Name: {yellow}{self.name}{reset}")
        print(f"Health: {yellow}{self.health}{reset}")
        print("=" * 40)
