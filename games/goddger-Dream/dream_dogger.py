import pygame, random, sys, os
from pygame.locals import *

WINDOW_WIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIE_MIN_SIZE = 10
BADDIE_MAX_SIZE = 40
BADDIE_MIN_SPEED = 1
BADDIE_MAX_SPEED = 8
ADD_NEW_BADDIE_RATE = 6
PLAYERMOVERATE = 5


def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Set up application
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)
font = pygame.font.SysFont(None, 48)

# set up images
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

# set up score
topScore = 0

def move_baddies_dows(baddies_1, reverseCheat_1, slowCheat_1):
    for b in baddies_1:
        if not reverseCheat_1 and not slowCheat_1:
            b['rect'].move_ip(0, b['speed'])
        elif reverseCheat_1:
            b['rect'].move_ip(0, -5)
        elif slowCheat_1:
            b['rect'].move_ip(0, 1)

# Move the baddies down.

def handle_mouse_or_keyboard_event():
    global reverseCheat, slowCheat, score

    if event.type == QUIT:
        terminate()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if (event.button == 1):
            reverseCheat = True
        if (event.button == 3):
            slowCheat = True

    if event.type == pygame.MOUSEBUTTONUP:
        if (event.button == 1):
            reverseCheat = False
            score = score / 2
        if (event.button == 3):
            slowCheat = False
            score = score / 2

    if event.type == KEYDOWN:
        if event.key == ord('z') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            reverseCheat = True
        if event.key == ord('x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 2):
            slowCheat = True

    if event.type == KEYUP:
        if event.key == ord('z') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            reverseCheat = False
            score = 0
        if event.key == ord('x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 2):
            slowCheat = False
            score = 0
        if event.key == K_ESCAPE:
            terminate()

    if event.type == MOUSEMOTION:
        # If the mouse moves, move the player where the cursor is.
        playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)


# global reverseCheat
# global slowCheat


def move_the_buddies_down(baddies_var, reverse_cheat_var, slow_cheat_var):
        # global b
    # Move the baddies down
    for b in baddies_var:
        if not reverse_cheat_var and not slow_cheat_var:
            b['rect'].move_ip(0, b['speed'])
        elif reverse_cheat_var:
            b['rect'].move_ip(0, -5)
        elif slow_cheat_var:
            b['rect'].move_ip(0, 1)


def delete_fallen_buddies():
    global b
    # Delete baddies that have fallen past the bottom.
    for b in baddies[:]:
        if b['rect'].top > WINDOWHEIGHT:
            baddies.remove(b)


def draw_black_game_window():
    # Draw the game world on the window.
    windowSurface.fill(BACKGROUNDCOLOR)


def draw_scores(current_score, max_score):
    # Draw the score and top score.
    drawText('Score: %s' % (current_score), font, windowSurface, 10, 0)
    drawText('Top Score: %s' % (max_score), font, windowSurface, 10, 40)


def draw_player():
    # Draw the player's rectangle
    windowSurface.blit(playerImage, playerRect)


def draw_all_baddies(baddies):
    # global b
    # Draw each baddie
    for b in baddies:
        windowSurface.blit(b['surface'], b['rect'])


while True:
    # set up the start of the game
    baddies = []
    score = 0
    playerRect.topleft = (WINDOW_WIDTH / 2, WINDOWHEIGHT - 50)
    # moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0

    while True: # the game loop runs while the game part is playing
        score += 1 # increase score

        for event in pygame.event.get():
            handle_mouse_or_keyboard_event()

        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADD_NEW_BADDIE_RATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIE_MIN_SIZE, BADDIE_MAX_SIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }
            baddies.append(newBaddie)


        # Move the mouse cursor to match the player.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        move_the_buddies_down(baddies, reverseCheat, slowCheat)

        delete_fallen_buddies()

        draw_black_game_window()
        draw_scores(score, topScore)
        draw_player()

        draw_all_baddies(baddies)

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(FPS)
