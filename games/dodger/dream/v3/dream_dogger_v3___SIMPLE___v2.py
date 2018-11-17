import pygame, random, sys
from pygame.constants import *


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

FPS = 40
ANIMAL_MIN_SIZE = 20
ANIMAL_MAX_SIZE = 200
ANIMAL_MIN_SPEED = 1
ANIMAL_MAX_SPEED = 8
ADD_NEW_ANIMAL_RATE = 20
PLAYER_MOVE_RATE = 5

# Set up application
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set up images
# playerImage = pygame.image.load('icons\ice_age_80_80.png')
# playerRect = playerImage.get_rect()

# set up score
animalAddCounter = 0


def get_animal_image():
    return pygame.image.load('icons\dinosaur.jpg')


def player_has_hit_animal(playerRect, animals):
    for an in animals:
        if playerRect.colliderect(an['rect']):
            return True
    return False


def move_the_animals_down(animals_var):
    # Move the animals down
    for an in animals_var:
        an['rect'].move_ip(0, an['speed'])


def delete_fallen_animals(animals_var):
    # Delete animals that have fallen past the bottom.
    for animal in animals_var[:]:
        if animal['rect'].top > WINDOW_HEIGHT:
            animals.remove(animal)


def draw_all_animals(animals):
    # Draw each animal
    for animal in animals:
        windowSurface.blit(animal['surface'], animal['rect'])



def wait_for_player_to_press_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # pressing escape quits
                    program_exit()
                return  # return to new game


def program_exit():
    pygame.quit()
    sys.exit()

def add_new_animal(animals_list):
    # Add new animals at the top of the screen
    animalSize = random.randint(ANIMAL_MIN_SIZE, ANIMAL_MAX_SIZE)
    newAnimal = {
        'rect': build_rectangle_at_random_top_position(animalSize),
        'speed': random.randint(ANIMAL_MIN_SPEED, ANIMAL_MAX_SPEED),
        'surface': pygame.transform.scale(get_animal_image(), (animalSize, animalSize)),
    }
    animals_list.append(newAnimal)


def build_rectangle_at_random_top_position(animalSize):
    return pygame.Rect(random.randint(0, WINDOW_WIDTH - animalSize), random.randint(0, WINDOW_HEIGHT - animalSize) - animalSize, animalSize, animalSize)


def new_animal_is_needed():
    # Increase counter that indicates that new animals are needed
    global animalAddCounter
    # if not reverseCheat and not slowCheat:
    animalAddCounter += 1
    if animalAddCounter == ADD_NEW_ANIMAL_RATE:
        animalAddCounter = 0
        return True
    return False




def draw_black_game_window(windowSurface):
    # Draw the game world on the window.
    windowSurface.fill(BACKGROUND_COLOR)


def add_new_animal_if_needed():
    global newAnimalsNeeded
    newAnimalsNeeded = new_animal_is_needed()
    # if newAnimalsNeeded:
    add_new_animal(animals)
        # newAnimalsNeeded = False

score = 0

while True:
    # set up the start of the game
    animals = []
    animalAddCounter = 0
    newAnimalsNeeded = False
    add_new_animal_if_needed()

    while True:  # the game loop runs while the game part is playing

        score += 1  # increase score

        # Move the mouse cursor to match the player.
        move_the_animals_down(animals)
        delete_fallen_animals(animals)
        draw_black_game_window(windowSurface)
        draw_all_animals(animals)

        # update screen
        pygame.display.update()


        mainClock.tick(FPS)
