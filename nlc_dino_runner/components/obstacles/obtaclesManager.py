import random
import pygame.time
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD #HIT_SOUND, GAME_OVER_SOUND #AÑADIDO



class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        obstacles_type = [Cactus(SMALL_CACTUS), Cactus(LARGE_CACTUS, 290), Bird(BIRD, random.randint(180, 260))]
        if len(self.obstacles_list) == 0 :
            self.obstacles_list.append(random.choice(obstacles_type))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)

            if game.player.hammer and game.player.hammer.rect.colliderect(obstacle.rect):
                self.obstacles_list.remove(obstacle)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                elif game.live_manager.lives > 1:
                        #HIT_SOUND.play()  # AÑADIDO
                    game.live_manager.reduce_lives()
                    game.player.shield = True
                    start_time = pygame.time.get_ticks()
                    game.player.shield_time_up = start_time + 1000
                else:
                    game.player.draw_dead(game.screen)
                    if game.points > game.highest_score:
                        game.player.draw_dead(game.screen)
                        game.highest_score = game.points
                    pygame.time.delay(1500)
                    game.playing = False
                    game.death_count += 1
                    #GAME_OVER_SOUND.play()
                    break

    def draw(self, screen):
        for obstacles in self.obstacles_list:
            obstacles.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
