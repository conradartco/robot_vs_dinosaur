from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.robot_one = Robot('Voltron')
        self.dino_one = Dinosaur('Little-Foot', 24)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print('\nWelcome to the battle arena!\nTwo compettitors enter, only one leaves...\n')
        welcome_input = input("Are you ready to begin? Y/N : ")
        if welcome_input == 'Y':
            print("That's the spirit! Now let's get ready to RUUUUMMMMBBBLLLEEEEEE!")
        else:
            print("Do you know how hard it was to get a dinosaur for this? They're literally extinct... the show MUST GO ON!")
        print(f'\nEntering the arena today is {self.robot_one.robot_name} vs. {self.dino_one.dino_name}.\nWho will win? Let the match commence!\n')

    def battle_phase(self):
        while self.robot_one.robot_health > 0 and self.dino_one.dino_health > 0:
            if self.dino_one.dino_health <=0 and self.robot_one.robot_health <=0:
                self.display_tie()
                break
            self.robot_one.arsenal()
            self.dino_one.dino_health = self.robot_one.attack(self.dino_one.dino_health)
            print(f"\n{self.dino_one.dino_name} is hit by {self.robot_one.robot_weapon.weapon_name} for {self.robot_one.robot_weapon.weapon_attack_pw} hit-points.")
            if self.dino_one.dino_health <= 0:
                self.display_winner()
                break
            print(f"{self.dino_one.dino_name} has {self.dino_one.dino_health} health remaining.")
            self.robot_one.robot_health = self.dino_one.attack(self.robot_one.robot_health)
            print(f"\n{self.robot_one.robot_name} is slashed by {self.dino_one.dino_name} for {self.dino_one.dino_attack_pw} hit-points.")
            if self.robot_one.robot_health <= 0:
                self.display_winner()
                break
            print(f"{self.robot_one.robot_name} has {self.robot_one.robot_health} health remaining.")

    def display_winner(self):
        if self.dino_one.dino_health <= 0:
            print(f"{self.dino_one.dino_name} has been mercilessly defeated!")
        elif self.robot_one.robot_health <= 0:
            print(f"{self.robot_one.robot_name} has been vanquished!")

    def display_tie(self):
        if self.dino_one.dino_health <= 0 and self.robot_one.robot_health <= 0:
            print(f"\n{self.dino_one.dino_name} and {self.robot_one.robot_name} have both been vanquished!\nI can't believe it, it's a TIE! Never a dull moment in the arena")