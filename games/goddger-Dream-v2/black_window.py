import pygame, random, sys
from pygame.locals import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 40
ADD_NEW_ANIMAL_RATE = 20


# Set up application

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My application')
pygame.mouse.set_visible(False)
font = pygame.font.SysFont(None, 48)


playerImage = pygame.image.load('icons\ice_age_80_80.png')
playerRect = playerImage.get_rect()


animal = pygame.image.load('icons\dinosaur.jpg')


# Exit application nicely
def exit_application():
    pygame.quit()
    sys.exit()


def handle_mouse_or_keyboard_event(event):

    # If the mouse moves, move the player where the cursor is.
    if event.type == MOUSEMOTION:
        playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)

    # Exit app on Escape
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        exit_application()


def handle_events():
    for event in pygame.event.get():
        handle_mouse_or_keyboard_event(event)


def draw_players_rectangle():
    windowSurface.blit(playerImage, playerRect)


# Draw the game world on the window.
def draw_black_game_window():
    windowSurface.fill(BACKGROUND_COLOR)


def player_has_hit_animal(playerRect, animal):
    if playerRect.colliderect(animal['rect']):
        return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXT_COLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_scores(current_score, max_score):
    # Draw the score and top score.
    drawText('Score: %s' % current_score, font, windowSurface, 10, 0)
    drawText('Top Score: %s' % max_score, font, windowSurface, 10, 40)


current_score = 0
top_score = 0
ANIMAL_MIN_SIZE = 20
ANIMAL_MAX_SIZE = 200
ANIMAL_MIN_SPEED = 1
ANIMAL_MAX_SPEED = 8

animalAddCounter = 0


# Every new game
def move_the_animals_down(animal_var):
    # Move the animals down
    animal_var['rect'].move_ip(0, animal_var['speed'])


def add_new_animal():
    animalSize = random.randint(ANIMAL_MIN_SIZE, ANIMAL_MAX_SIZE)
    newAnimal = {
        'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - animalSize), 0 - animalSize, animalSize, animalSize),
        'speed': random.randint(ANIMAL_MIN_SPEED, ANIMAL_MAX_SPEED),
        # 'surface': pygame.transform.scale(animalImage, (animalSize, animalSize)),
        'surface': pygame.transform.scale(animal, (animalSize, animalSize)),
    }
    animals.append(newAnimal)


def delete_fallen_animals():
    # Delete animals that have fallen past the bottom.
    for animal in animals[:]:
        if animal['rect'].top > WINDOW_HEIGHT:
            animals.remove(animal)


def new_animal_needed():
    # Increase counter that indicates that new animals are needed
    global animalAddCounter
    animalAddCounter += 1
    if animalAddCounter == ADD_NEW_ANIMAL_RATE:
        animalAddCounter = 0
        return True
    return False

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
            'surface': pygame.transform.scale(animal, (animalSize, animalSize)),
        }
        animals_list.append(newAnimal)



while True:
    animals = []
    current_score = 0
    animalAddCounter = 0
    newAnimalsNeeded = False
    # Repeat every 40 FSP (25 ms)
    while True:
        handle_events()
        newAnimalsNeeded = new_animal_needed()
        if newAnimalsNeeded:
            add_new_animals_if_needed(animals, newAnimalsNeeded)
            newAnimalsNeeded = False


        # Move the mouse cursor to match the player.
        # pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        move_the_animals_down(animals)
        delete_fallen_animals()

        draw_black_game_window()
        draw_players_rectangle()
        draw_scores(current_score, top_score)

        pygame.display.update()

        if player_has_hit_animal(playerRect, animal):
            current_score += 1

        mainClock.tick(FPS)


