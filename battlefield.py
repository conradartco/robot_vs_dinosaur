from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot_one = Robot('Voltron')
        self.dino_one = Dinosaur('Little-Foot', 24)

    def run_game(self):
        self.display_welcome
        print(f'\nEntering the arena today is {self.robot_one.robot_name} vs. {self.dino_one.dino_name}.\nWho will win? Let the match commence!\n')
        self.battle_phase
        self.display_winner

    def display_welcome(self):
        print('\nWelcome to the battle arena!\nTwo compettitors enter, only one leaves...\n')

    def battle_phase(self):
        self.hit = self.robot_one.attack(self.dino_one)
        pass

    def display_winner(self):
        pass