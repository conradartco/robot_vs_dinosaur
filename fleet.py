from weapon import Weapon

class Fleet:
    def __init__(self, robo_name):
        # list of 3 robots to be chosen to fight 3 dinosaurs
       self.robo_name = robo_name
       self.robot_health = int(125)
       self.fleet_weapon = Weapon('Robo-Pistol', int(35))

    def attack_remix(self, herd):
        # returns health level remaining
        health_lvl = (int(herd) - self.fleet_weapon.weapon_attack_pw)
        return health_lvl
