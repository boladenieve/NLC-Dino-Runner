
from nlc_dino_runner.components.obstacles.obstacles import Obstacles



class Bird(Obstacles):
    def __init__(self, image, Y):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = Y
