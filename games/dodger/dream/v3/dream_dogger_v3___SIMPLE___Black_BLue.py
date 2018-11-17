import pygame, random, sys
from pygame.constants import *


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
BACKGROUND_COLOR_2 = (40, 50, 150)


# Set up application
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_black_game_window(windowSurface, color):
    windowSurface.fill(color)


while True:
    # set up the start of the game
    indicator = False

    while True:

        if (indicator):
            draw_black_game_window(windowSurface, BACKGROUND_COLOR)
        else:
            draw_black_game_window(windowSurface, BACKGROUND_COLOR_2)
        indicator = not indicator
        pygame.display.update()
        mainClock.tick(2)
