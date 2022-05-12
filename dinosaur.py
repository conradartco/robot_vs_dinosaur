class Dinosaur:
    def __init__(self, name, attack_power):
        self.dino_name = name
        self.dino_attack_pw = int(attack_power)
        self.dino_health = int(100)

    def attack(self, robot):
        health_lvl = (int(robot) - self.dino_attack_pw)
        return health_lvl
