import random


class Player:
    def __init__(self):
        self.inventory = []
        self.strength = 50
        self.level = 1
        self.gold = 100
        self.stamina = 100
        self.progress = 0
        self.health = 100
        self.achievements = []
        self.skill_points = 0
        self.skills = {"Power Lifter": 0, "Runner": 0, "BodyBuilder": 0}

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def increase_strength(self, amount):
        self.strength += amount
        if self.strength >= 100*self.level:
            self.level_up()
            self.gain_skill_point()

    def increase_health(self, amount):
        self.health += amount
        if self.health >= 101*self.level:
            self.level_up()
            self.gain_skill_point()

    def increase_max_stamina(self, amount):
        self.stamina += amount
        if self.stamina >= 101*self.level:
            self.level_up()
            self.gain_skill_point()

    def level_up(self):
        self.level += 1
        print(f"Congratulations! You have reached level {self.level}!")

    def decrease_gold(self, amount):
        self.gold -= amount
        if self.gold < 0:
            self.gold = 0

    def increase_gold(self, amount):
        self.gold += amount

    def decrease_stamina(self, amount):
        self.stamina -= amount
        if self.stamina <= 0:
            print("You are too tired to continue. You should rest.")
            self.stamina = 0
            return False
        elif self.stamina > 100:
            self.stamina = 100
            return True
        return True

    def train(self, type_of_training):
        if type_of_training == "strength":
            self.increase_strength(10)
            self.progress += 10
        elif type_of_training == "cardio":
            self.increase_strength(5)
            self.progress += 5
    def motivate(self):
        with open("motivational_quotes.txt", "r") as file:
            quotes = file.readlines()

        quotes = [quote.strip() for quote in quotes]

        selected_quote = random.choice(quotes)
        print(selected_quote)
        
        input("press enter to continue")

        

    def add_achievement(self, achievement):
        self.achievements.append(achievement)
        print(f"Achievement Unlocked: {achievement}")

    def check_achievements(self):
        if self.strength >= 100:
            if "Strength Master" not in self.achievements:
                self.add_achievement("Strength Master")
        if self.gold >= 500:
            if "Gold Hoarder" not in self.achievements:
                self.add_achievement("Gold Hoarder")

    def gain_skill_point(self):
        self.skill_points += 1
        print("You gained a skill point!")

    def use_skill_point(self, skill):
        if self.skill_points > 0 and skill in self.skills:
            self.skills[skill] += 1
            self.skill_points -= 1
            print(f"You upgraded {skill} skill to level {self.skills[skill]}!")
            if skill == "Power Lifter":
                self.increase_strength(50)
            elif skill == "Runner":
                self.increase_max_stamina(50)
            elif skill == "BodyBuilder":
                self.increase_health(50)
        else:
            print("You don't have enough skill points or invalid skill.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("You have been defeated by the Gym Leader. Better luck next time!")
            print("Do you want to continue your journey?")
            print("1. Yes")
            print("2. No")
            choice = input("What do you choose? (1/2): ")
            if choice == "1":
                pass
            elif choice == "2":
                print("See you again later!")
                exit()

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"   - {self.cyan}{item}{self.reset}")

    def show_stats(self):
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.cyan = "\033[36m"
        self.magenta = "\033[35m"
        self.reset = "\033[0m"

        print(f"{self.green}Player Stats{self.reset}".center(40, "="))
        print(f"Level: {self.yellow}{self.level}{self.reset}")
        print(f"Strength: {self.yellow}{self.strength}{self.reset}")
        print(f"Gold: {self.yellow}{self.gold}{self.reset}")
        print(f"Stamina: {self.yellow}{self.stamina}{self.reset}")
        print(f"Health: {self.yellow}{self.health}{self.reset}")
        print(f"Progress: {self.yellow}{self.progress}{self.reset}")
        print(f"Achievements: {self.cyan}{', '.join(self.achievements)}{self.reset}")
        print(f"Skill Points: {self.yellow}{self.skill_points}{self.reset}")
        print("Skills:")
        for skill, level in self.skills.items():
            print(f"   - {self.cyan}{skill}{self.reset}: Level {self.yellow}{level}{self.reset}")
        self.show_inventory()

        print("=" * 40)

    def show_battle_stats(self):
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.cyan = "\033[36m"
        self.magenta = "\033[35m"
        self.reset = "\033[0m"

        print(f"{self.green}Player Stats{self.reset}".center(40, "="))
        print(f"Health: {self.yellow}{self.health}{self.reset}")
        print(f"Strength: {self.yellow}{self.strength}{self.reset}")
        print(f"Stamina: {self.yellow}{self.stamina}{self.reset}")

        print("=" * 40)
