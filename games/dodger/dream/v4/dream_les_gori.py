import easygui
import pygame, random, sys
from pygame.constants import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

pygame.display.set_caption('Dodger')
font = pygame.font.SysFont(None, 48)


def draw_player():
    playerImage = pygame.image.load('icons\ice_age_80_80.png')
    playerRect = playerImage.get_rect()
    windowSurface.blit(playerImage, playerRect)


pygame.init()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



# def draw_text(text, font, surface, x, y):
#     textobj = font.render(text, 1, TEXT_COLOR)
#     textrect = textobj.get_rect()
#     textrect.topleft = (x, y)
#     surface.blit(textobj, textrect)
#
#
# def draw_scores(window_surface, current_score, max_score):
#     # score coordinates:
#     X_1 = 10
#     Y_1 = 0
#     # top score coordinates:
#     X_2 = 10
#     Y_2 = 40
#     draw_text('Score: %s' % (current_score), font, window_surface, X_1, Y_1)
#     draw_text('Top Score: %s' % (max_score), font, window_surface, X_2, Y_2)




myvar = easygui.enterbox("What, is your favorite color?")

myvar2 = easygui.enterbox(myvar + " - is your favorite color")

# inp = inputbox.ask(screen, 'Message')

