import random

import pygame.time

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.large_cactus import LargeCactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []


    def update(self, game):
        small_or_long = random.randint(0, 1)
        if len(self.obstacles_list) == 0 and small_or_long == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))
        elif len(self.obstacles_list) == 0 and small_or_long == 1:
            self.obstacles_list.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.points > game.highest_score:
                    game.highest_score = game.points
                pygame.time.delay(2000)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacles in self.obstacles_list:
            obstacles.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
