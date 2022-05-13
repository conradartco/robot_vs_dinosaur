from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = int(120)
        self.robot_weapon = Weapon('Varatha, the Eternal Spear', int(38))
        self.robot_arsenal = []

    def attack(self, dinosaur):
        health_lvl = (int(dinosaur) - self.robot_weapon.weapon_attack_pw)
        return health_lvl

    def arsenal(self):
        self.robot_arsenal.append(Weapon('Varatha, the Eternal Spear', int(38)))
        self.robot_arsenal.append(Weapon('Sword of the Stone', int(32)))
        self.robot_arsenal.append(Weapon('Bloodstone Bludgeon', int(45)))
        self.arsenal_select = input(f"Select your weapon:\nA) Varatha, the Eternal Spear (38 DPS)\nB) Sword of the Stone (32 DPS)\nC) Bloodstone Bludgeon (45 DPS)\nAnswer: ")
        if self.arsenal_select == 'A':
            self.robot_weapon = self.robot_arsenal[0]
        elif self.arsenal_select == 'B':
            self.robot_weapon = self.robot_arsenal[1]
        elif self.arsenal_select == 'C':
            self.robot_weapon = self.robot_arsenal[2]