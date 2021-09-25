from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import SCREEN_WIDTH



class Obstacles(Sprite):
    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, obstacles_list):
        if len(self.image) == 2:
            self.update_bird(game_speed)
        else:
            self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles_list.pop()

    def draw(self, screen):
        if len(self.image) == 2:
            self.draw_bird(screen)
        screen.blit(self.image[self.obstacle_type], self.rect)

    def update_bird(self, game_speed):
        if self.step_index >= 10:
            self.step_index = 0
        self.rect.x -= game_speed + game_speed * 0.1
        self.step_index += 1

    def draw_bird(self, screen):
        if self.step_index > 5:
            self.obstacle_type = 0
        else:
            self.obstacle_type = 1
