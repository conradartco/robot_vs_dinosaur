from dinosaur import Dinosaur
from robot import Robot
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.robot_one = Robot('Voltron')
        self.dino_one = Dinosaur('Little-Foot', 24)
        self.herd_1 = Herd('Martha', 22)
        self.herd_2 = Herd('Bartha', 28)
        self.herd_3 = Herd('Sue', 26)
        self.fleet_1 = Fleet('Century-Bot Alpha')
        self.fleet_2 = Fleet('Century-Bot Bravo')
        self.fleet_3 = Fleet('Century-Bot Charlie')

    # this will call the game, and decide if the user wants to see a 1v1 or 3v3 battle
    def run_game(self):
        print("\n\x1B[3m You hear crowds cheering, explosions and gasps coming from the colosseum ahead.\nA ticket counter is ahead, behind it are two separate entrances.\x1B[0m")
        self.path_choice = input("\nWelcome to the Colosseum of Ages!\nPlease select the show you would like to see:\nA) 1v1 Robot vs. Dinosaur\nB) 3v3 Smackdown Extravaganza\nAnswer: ")
        if self.path_choice == 'A':
            self.display_welcome()
            self.battle_phase()
        elif self.path_choice == 'B':
            self.display_remix()
            self.battle_phase_remix()

    # this is the intro to the 3v3 match
    def display_remix(self):
        print("\nWelcome to the Clash of the Ages, 3 on 3, Robots vs. Dinosaurs Smackdown Extravaganza mama.\nWill anyone survive our match today? Who can never be sure.\n")
        remix_input = input("Are you ready to begin? Y/N : ")
        if remix_input == 'Y':
            print("Excellent! Now let's get ready to RUUUUMMMMBBBLLLEEEEEE!")
        else:
            print("Too late! We've already locked the gates behind you.\nThe show MUST GO ON!")
        print(f"\nAt the South gate we have our dinosaur competitors: {self.herd_1.dino_name}, {self.herd_2.dino_name} and {self.herd_3.dino_name}\nAt the North gate, we have our fearsome robot militia, the Century-Bot Corps.")

    # this is the intro the the 1v1 match
    def display_welcome(self):
        print('\nWelcome to the battle arena!\nTwo compettitors enter, only one leaves...\n')
        welcome_input = input("Are you ready to begin? Y/N : ")
        if welcome_input == 'Y':
            print("That's the spirit! Now let's get ready to RUUUUMMMMBBBLLLEEEEEE!")
        else:
            print("Do you know how hard it was to get a dinosaur for this?\nThey're quite literally extinct... the show MUST GO ON!")
        print(f'\nEntering the arena today is {self.robot_one.robot_name} vs. {self.dino_one.dino_name}.\nWho will win? Let the match commence!\n')

    # 1v1 battle sequence
    def battle_phase(self):
        while self.robot_one.robot_health > 0 and self.dino_one.dino_health > 0:
            if self.dino_one.dino_health <=0 and self.robot_one.robot_health <= 0:
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

    # 3v3 battle sequence
    def battle_phase_remix(self):
        self.herd_total_hp = (self.herd_1.dino_health + self.herd_2.dino_health + self.herd_3.dino_health)
        self.fleet_total_hp = (self.fleet_1.robot_health + self.fleet_2.robot_health + self.fleet_3.robot_health)
        while self.herd_total_hp > 0 and self.fleet_total_hp > 0:
            if self.fleet_total_hp <= 0 and self.herd_total_hp <= 0:
                self.display_tie()
                break
            self.fleet_attack(self.herd_1.dino_health, self.herd_2.dino_health, self.herd_3.dino_health)
            self.herd_total_hp = (self.herd_1.dino_health + self.herd_2.dino_health + self.herd_3.dino_health)
            if self.herd_total_hp <= 0:
                self.display_winner()
                break
            print(f"The herd has {self.herd_total_hp} hit-points remaining")
            self.herd_attack(self.fleet_1.robot_health, self.fleet_2.robot_health, self.fleet_3.robot_health)
            self.fleet_total_hp = (self.fleet_1.robot_health + self.fleet_2.robot_health + self.fleet_3.robot_health)
            if self.fleet_total_hp <= 0:
                self.display_winner()
                break
            print(f"The Century-Corps has {self.fleet_total_hp} hit-points remaining")
        
    def fleet_attack(self, dino_1_hp, dino_2_hp, dino_3_hp):
        self.herd_1.dino_health = (dino_1_hp - self.fleet_1.fleet_weapon.weapon_attack_pw)
        self.herd_2.dino_health = (dino_2_hp - self.fleet_2.fleet_weapon.weapon_attack_pw)
        self.herd_3.dino_health = (dino_3_hp - self.fleet_3.fleet_weapon.weapon_attack_pw)
        print(f"{self.herd_1.dino_name}, {self.herd_2.dino_name}, and {self.herd_3.dino_name} are all blasted by {self.fleet_1.fleet_weapon.weapon_name}'s for {self.fleet_1.fleet_weapon.weapon_attack_pw} hit-points each.")

    def herd_attack(self, robo_1_hp, robo_2_hp, robo_3_hp):
        self.fleet_1.robot_health = (robo_1_hp - self.herd_1.dino_pwr)
        print(f"{self.herd_1.dino_name} slashes {self.fleet_1.robo_name} for {self.herd_1.dino_pwr} hit-points.")
        self.fleet_2.robot_health = (robo_2_hp - self.herd_2.dino_pwr)
        print(f"{self.herd_2.dino_name} tears at {self.fleet_2.robo_name} for {self.herd_2.dino_pwr} hit-points.")
        self.fleet_3.robot_health = (robo_3_hp - self.herd_3.dino_pwr)
        print(f"{self.herd_3.dino_name} chomps on {self.fleet_3.robo_name} for {self.herd_3.dino_pwr} hit-points.")
        

    def display_winner(self):
        if self.dino_one.dino_health <= 0:
            print(f"{self.dino_one.dino_name} has been mercilessly defeated!")
        elif self.robot_one.robot_health <= 0:
            print(f"{self.robot_one.robot_name} has been vanquished!")
        elif self.fleet_total_hp <= 0:
            print("The robot militia has been vanquised! Long reign the dinosaurs!")
        elif self.herd_total_hp <= 0:
            print("The dinosaurs have been mercilessly defeated. The Century-Bot's claim another victim...")

    def display_tie(self):
        if self.dino_one.dino_health <= 0 and self.robot_one.robot_health <= 0:
            print(f"\n{self.dino_one.dino_name} and {self.robot_one.robot_name} have both been vanquished!\nI can't believe it, it's a TIE! Never a dull moment in the arena")
        elif self.fleet_total_hp <= 0 and self.herd_total_hp <= 0:
            print("It's...a tie?")