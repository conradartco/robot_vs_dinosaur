import random

class Herd:
    def __init__(self, dino_name, dino_pwr):
        # list of 3 dinosaurs to be chosen to fight 3 robots
        self.dino_name = dino_name
        self.dino_pwr = int(dino_pwr)
        self.dino_health = random.randrange(150, 200)

    def attack_remix(self, fleet):
        # returns remaining health level 
        health_lvl = (int(fleet) - self.dino_pwr)
        return health_lvl