import random
from nlc_dino_runner.components.obstacles.obstacles import Obstacles



class Cactus(Obstacles):
    def __init__(self, image, Y = 315):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = Y
