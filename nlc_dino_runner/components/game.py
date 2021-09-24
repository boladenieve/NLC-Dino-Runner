import pygame

from nlc_dino_runner.components.lives.lives import Live
from nlc_dino_runner.components.lives.livesManager import LiveManager
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.components.obstacles.obtaclesManager import ObstaclesManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, BG, FPS#, GAME_THEME
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.components.hammer import Hammer


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.player = Dinosaur()
        self.obstacles_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.highest_score = 0
        self.live = Live()
        self.live_manager = LiveManager()

    def run(self):
        self.obstacles_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.live_manager.reset_lives()
        self.game_speed = 20
        self.points = 0
        self.playing = True
        #GAME_THEME.play()  # AÑADIDO
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacles_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacles_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.live_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
                #GAME_THEME.stop()

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        #aqui debe mostrarse el menu

        self.print_menu_elements()

        pygame.display.update()

        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT / 2
        if self.death_count == 0:
            message = "Press any Key to Start"
        else:
            message = "Press any Key to Restart"
        text, text_rect = text_utils.get_centered_message(message)
        self.screen.blit(text, text_rect)

        death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count), height=half_screen_height + 50)
        self.screen.blit(death_score, death_score_rect)

        highest, highest_rect = text_utils.get_centered_message("Highest score: " + str(self.highest_score), height=560 , width= 170)
        self.screen.blit(highest, highest_rect)

        #Imprimiendo dinosaurio de portada
        self.screen.blit(ICON, ((SCREEN_WIDTH / 2) - 40, (SCREEN_HEIGHT / 3.6)))
