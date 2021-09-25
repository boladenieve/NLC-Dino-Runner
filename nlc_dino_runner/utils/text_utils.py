import pygame

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)

def get_score_element(points, color = BLACK_COLOR):
    font = pygame.font.Font(FONT_STYLE, 24)
    text = font.render("Points: " + str(points), True, color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return (text, text_rect)

def get_centered_message(message, width = SCREEN_WIDTH//2, height = SCREEN_HEIGHT//2, size = 35, text_color = BLACK_COLOR):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(message, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return (text, text_rect)
