import pygame, random, sys, os
from pygame.locals import *

WINDOW_WIDTH = 1000
WINDOWHEIGHT = 800
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
ANIMAL_MIN_SIZE = 20
ANIMAL_MAX_SIZE = 200
ANIMAL_MIN_SPEED = 1
ANIMAL_MAX_SPEED = 8
ADD_NEW_ANIMAL_RATE = 20
PLAYERMOVERATE = 5

# Set up application
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)
font = pygame.font.SysFont(None, 48)

# set up images
# playerImage = pygame.image.load('icons\player.png')
# playerImage = pygame.image.load('icons\ice_age.png')
playerImage = pygame.image.load('icons\ice_age_80_80.png')

playerRect = playerImage.get_rect()
# animalImage = pygame.image.load('baddie.png')

animalImage_1 = pygame.image.load('icons\dinosaur.jpg')
animalImage_2 = pygame.image.load('icons\ezik_v_tumane.png')
animalImage_3 = pygame.image.load('icons\panda.jpg')
animalImage_4 = pygame.image.load('icons\penguine.jpg')

all_animals = [animalImage_1, animalImage_2, animalImage_3, animalImage_4]

def getRandomAnimal():
    return all_animals[random.randint(0, 3)]


# set up score
topScore = 0
animalAddCounter = 0


def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # pressing escape quits
                    terminate()
                return


def playerHasHitAnimal(playerRect, animals):
    for b in animals:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def move_animals_dows(animals_1, reverseCheat_1, slowCheat_1):
    for b in animals_1:
        if not reverseCheat_1 and not slowCheat_1:
            b['rect'].move_ip(0, b['speed'])
        elif reverseCheat_1:
            b['rect'].move_ip(0, -5)
        elif slowCheat_1:
            b['rect'].move_ip(0, 1)


# Move the animals down.

def handle_mouse_or_keyboard_event(event):
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


def move_the_animals_down(animals_var, reverse_cheat_var, slow_cheat_var):
    # global b
    # Move the animals down
    for b in animals_var:
        if not reverse_cheat_var and not slow_cheat_var:
            b['rect'].move_ip(0, b['speed'])
        elif reverse_cheat_var:
            b['rect'].move_ip(0, -5)
        elif slow_cheat_var:
            b['rect'].move_ip(0, 1)


def delete_fallen_animals():
    global b
    # Delete animals that have fallen past the bottom.
    for animal in animals[:]:
        if animal['rect'].top > WINDOWHEIGHT:
            animals.remove(animal)


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


def draw_all_animals(animals):
    # global b
    # Draw each animal
    for b in animals:
        windowSurface.blit(b['surface'], b['rect'])


def get_mouse_keyboard_events():
    # global event
    for event in pygame.event.get():
        handle_mouse_or_keyboard_event(event)


def add_new_animals_if_needed(animals_list, newAnimalsNeeded):
    # global animalAddCounter
    # global newanimalsNeeded
    # Add new animals at the top of the screen, if needed.
    # if animalAddCounter == ADD_NEW_ANIMAL_RATE:
    if newAnimalsNeeded:
        # animalAddCounter = 0
        newAnimalsNeeded = False
        animalSize = random.randint(ANIMAL_MIN_SIZE, ANIMAL_MAX_SIZE)
        newAnimal = {
            'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - animalSize), 0 - animalSize, animalSize, animalSize),
            'speed': random.randint(ANIMAL_MIN_SPEED, ANIMAL_MAX_SPEED),
            # 'surface': pygame.transform.scale(animalImage, (animalSize, animalSize)),
            'surface': pygame.transform.scale(getRandomAnimal(), (animalSize, animalSize)),
        }
        animals_list.append(newAnimal)


def new_animal_needed():
    # Increase counter that indicates that new animals are needed
    global animalAddCounter
    if not reverseCheat and not slowCheat:
        animalAddCounter += 1
        if animalAddCounter == ADD_NEW_ANIMAL_RATE:
            animalAddCounter = 0
            return True
    return False

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return


while True:
    # set up the start of the game
    animals = []
    score = 0
    # playerRect.topleft = (WINDOW_WIDTH / 2, WINDOWHEIGHT - 50)
    reverseCheat = slowCheat = False
    animalAddCounter = 0
    newAnimalsNeeded = False

    while True:  # the game loop runs while the game part is playing
        score += 1  # increase score

        get_mouse_keyboard_events()
        newAnimalsNeeded = new_animal_needed();
        if newAnimalsNeeded:
            add_new_animals_if_needed(animals, newAnimalsNeeded)
            newAnimalsNeeded = False

        # Move the mouse cursor to match the player.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        move_the_animals_down(animals, reverseCheat, slowCheat)
        delete_fallen_animals()
        draw_black_game_window()
        draw_scores(score, topScore)
        draw_player()
        draw_all_animals(animals)

        # update screen
        pygame.display.update()

        # Check if any of the animals have hit the player.
        if playerHasHitAnimal(playerRect, animals):
            if score > topScore:
                topScore = score  # set new top score
            draw_black_game_window()
            draw_player()
            pygame.display.update()
            waitForPlayerToPressKey()
            break

        mainClock.tick(FPS)
