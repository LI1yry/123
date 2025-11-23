import sys

import pygame

from models import State

pygame.init()
pygame.display.set_caption("Крестики-нолики")

WIDTH, HEIGHT = 400, 500
BG_COLOR = (28, 170, 156)

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_COLOR = (19, 128, 117)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 24

LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SPACE = 55
CIRCLE_RADIUS = 40
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

WHITE = (255, 255, 255)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

play_button_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH,
                               BUTTON_HEIGHT)

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    def check_events(self):
        print()


