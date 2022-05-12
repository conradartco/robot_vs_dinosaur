from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot_one = Robot('Voltron')
        self.dino_one = Dinosaur('Little-Foot', 24)

    def run_game(self):
        self.display_welcome()
        self.battle_start = True
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to the battle arena!\nTwo compettitors enter, only one leaves...\n')
        print(f'\nEntering the arena today is {self.robot_one.robot_name} vs. {self.dino_one.dino_name}.\nWho will win? Let the match commence!\n')

    def battle_phase(self):
        # this needs to pit the dinosaur against the robot
        # self.hit = self.robot_one.attack(self.dino_one)
        while self.battle_start is True:
            self.dino_one.dino_health = self.robot_one.attack(self.dino_one.dino_health)
            self.robot_one.robot_health = self.dino_one.attack(self.robot_one.robot_health)
            if self.dino_one.dino_health > 0:
                print(self.dino_one.dino_health)
            elif self.robot_one.robot_health > 0:
                print(self.robot_one.robot_health)
            elif self.dino_one.dino_health <= 0:
                print(f"{self.dino_one.dino_name} has been mercilessly defeated!")
                self.battle_start == False
            elif self.robot_one.robot_health <= 0:
                self.battle_start == False
                print(f"{self.robot_one.robot_name} has been vanquished!")
             
    def display_winner(self):
        if self.dino_one.dino_health <= 0:
            print(f"{self.dino_one.dino_name} has been mercilessly defeated!")
        elif self.robot_one.robot_health <= 0:
            print(f"{self.robot_one.robot_name} has been vanquished!")
