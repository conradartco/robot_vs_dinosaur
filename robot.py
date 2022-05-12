from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = int(100)
        self.robot_weapon = Weapon('Varatha, the Eternal Spear', int(35))

    def attack(self, dinosaur):
        # this needs to 
        self.attack_init = dinosaur
        pass