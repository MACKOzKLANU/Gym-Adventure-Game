import os
import time
import random
from player import Player

from boss import Boss


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def introduction():
    print("Welcome to the Gym Adventure Game!")
    print("You are at the gym with the goal of reaching maximum strength.")
    print("You start your adventure in the locker room.")
    time.sleep(10)
    clear_console()


def choice_one():
    player.show_stats()
    print("You have five choices:")
    print("1. Go to the weightlifting area")
    print("2. Go to the cardio area")
    print("3. Visit the shop")
    print("4. Rest and recover stamina")
    print("5. Get motivated")
    choice = input("What do you choose? (1/2/3/4/5): ")
    clear_console()
    if choice == "1":
        weightlifting_area()
    elif choice == "2":
        cardio_area()
    elif choice == "3":
        visit_shop()
    elif choice == "4":
        rest()
    elif choice == "5":
        player.motivate()
    else:
        print("Invalid choice. Try again.")
        choice_one()


def choice_two():
    player.show_stats()
    print("You can choose what to drink:")
    if not player.inventory:
        print("You have nothing to drink")
    else:
        if "protein shake" in player.inventory:
            print("1. Drink the protein shake")
        if "water bottle" in player.inventory:
            print("2. Drink the water")
    print("3. Do not drink")
    if player.skill_points > 0:
        print("4. Upgrade Skills")
        choice = input("What do you choose? (1/2/3/4): ")
    else:
        choice = input("What do you choose? (1/2/3): ")

    clear_console()
    if choice == "1" and "protein shake" in player.inventory:
        player.use_item("protein shake")
        player.increase_strength(30)
        print("You drank the protein shake and increased your strength!")
        player.check_achievements()
        time.sleep(3)
        clear_console()
        choice_three()
    elif choice == "2" and "water bottle" in player.inventory:
        player.use_item("water bottle")
        player.increase_strength(10)
        print("You drank the water and increased your strength!")
        player.check_achievements()
        time.sleep(3)
        clear_console()
        choice_three()
    elif choice == "3":
        player.increase_strength(5)
        print("You increased your strength!")
        player.check_achievements()
        time.sleep(3)
        clear_console()
        choice_three()
    elif choice == "4" and player.skill_points > 0:
        print("Choose a skill to upgrade:")
        print("1. Power Lifter")
        print("2. Runner")
        print("3. BodyBuilder")
        skill_choice = input("What do you choose? (1/2/3): ")
        if skill_choice == "1":
            player.use_skill_point("Power Lifter")
        elif skill_choice == "2":
            player.use_skill_point("Runner")
        elif skill_choice == "3":
            player.use_skill_point("BodyBuilder")
        else:
            print("Invalid choice.")
        choice_two()
    else:
        print("Invalid choice. Try again.")
        choice_two()


def choice_three():
    player.show_stats()
    print("You have two choices:")
    print("1. Continue working out")
    print("2. Face the final boss")
    choice = input("What do you choose? (1/2): ")
    clear_console()
    if choice == "1":
        choice_one()
    elif choice == "2":
        final_boss_battle()
    else:
        print("Invalid choice. Try again.")
        choice_three()


def weightlifting_area():
    if player.decrease_stamina(20):
        for i in range(10):
            input("Press Enter to lift weights...")
        print("You have completed your weightlifting session.")
        player.increase_gold(10)
        print("You earned 10 gold for your hard work!")
        rob_rats = input("Do you want to rob the skinny rats? (yes/no): ")
        if rob_rats.lower() == "yes":
            robbed_gold = random.randint(1, 50)
            player.increase_gold(robbed_gold)
            print(f"You robbed the skinny rats and earned {robbed_gold} gold!")
        elif rob_rats.lower() == "no":
            robbed_gold = random.randint(1, 50)
            player.decrease_gold(robbed_gold)
            print(f"Skinny rats robbed you and you lost {robbed_gold} gold!")

        player.check_achievements()
        time.sleep(3)
        clear_console()
        choice_two()
    else:
        time.sleep(3)
        clear_console()
        choice_three()


def cardio_area():
    if player.decrease_stamina(30):
        for i in range(10):
            input("Press Enter to run on the treadmill...")
        print("You have completed your cardio session.")
        player.increase_gold(10)
        print("You earned 10 gold and increased your strength by 10 for your hard work!")
        player.check_achievements()
        time.sleep(3)
        clear_console()
        choice_two()
    else:
        time.sleep(3)
        clear_console()
        choice_three()


def visit_shop():
    print(f"You have {player.gold} gold.")
    print("You visit the shop. You can buy a protein shake for 50 gold or a water bottle for 30 gold.")
    print("You have three choices:")
    print("1. Buy a protein shake")
    print("2. Buy a water bottle")
    print("3. Go back to the main menu")
    choice = input("What do you choose? (1/2/3): ")
    clear_console()
    if choice == "1":
        if player.gold >= 50:
            player.decrease_gold(50)
            player.add_item("protein shake")
            print("You bought a protein shake.")
        else:
            print("You don't have enough gold.")
    elif choice == "2":
        if player.gold >= 30:
            player.decrease_gold(30)
            player.add_item("water bottle")
            print("You bought a water bottle.")
        else:
            print("You don't have enough gold.")
    elif choice == "3":
        choice_one()
        return
    else:
        print("Invalid choice. Try again.")
        visit_shop()


def rest():
    print("You take a rest and recover your stamina.")
    player.stamina = 100
    time.sleep(3)
    clear_console()


def final_boss_battle():
    boss = Boss("Gym Leader", 1000)
    print("You face the final boss: The Gym Leader!")
    while boss.health > 0 and player.health > 0:
        player.show_battle_stats()
        boss.show_stats()
        print("You have two choices:")
        print("1. Attack the boss")
        print("2. Rest and recover stamina")
        choice = input("What do you choose? (1/2): ")
        clear_console()
        if choice == "1":
            boss.take_damage(player.strength)
            print(f"You attack the boss and deal {player.strength} damage!")
            if boss.health > 0:
                boss.attack(player)
        elif choice == "2":
            rest()
        else:
            print("Invalid choice. Try again.")


player = Player()


def main():
    introduction()
    while True:
        choice_one()


if __name__ == "__main__":
    main()
