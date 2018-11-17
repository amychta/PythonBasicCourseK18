import pygame, random, sys
from pygame.constants import *

# from games.dodger.dream.v3.events_handler import waitForPlayerToPressKey, handle_mouse_or_keyboard_event
# from games.dodger.dream.v3.windows_operations_v3 import create_window, draw_scores, window_height, \
#     build_rectangle_at_random_top_position, draw_black_game_window
# from games.dodger.dream.v3.events import waitForPlayerToPressKey, handle_mouse_or_keyboard_event

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
pygame.display.set_caption('Dodger')
font = pygame.font.SysFont(None, 48)

pygame.mouse.set_visible(False)

# set up images
playerImage = pygame.image.load('icons\ice_age_80_80.png')
playerRect = playerImage.get_rect()

# set up score
topScore = 0
animalAddCounter = 0


def get_animal():
    return pygame.image.load('icons\dinosaur.jpg')


def player_has_hit_animal(playerRect, animals):
    for an in animals:
        if playerRect.colliderect(an['rect']):
            return True
    return False


def move_the_animals_down(animals_var):
    # Move the animals down
    for an in animals_var:
        # if not reverse_cheat_var and not slow_cheat_var:
            an['rect'].move_ip(0, an['speed'])
        # elif reverse_cheat_var:
        #     an['rect'].move_ip(0, -5)
        # elif slow_cheat_var:
        #     an['rect'].move_ip(0, 1)


def delete_fallen_animals(animals_var):
    # Delete animals that have fallen past the bottom.
    for animal in animals_var[:]:
        if animal['rect'].top > WINDOW_HEIGHT:
            animals.remove(animal)


def draw_player():
    # Draw the player's rectangle
    windowSurface.blit(playerImage, playerRect)


def draw_all_animals(animals):
    # Draw each animal
    for animal in animals:
        windowSurface.blit(animal['surface'], animal['rect'])


def get_mouse_keyboard_events():
    for event in pygame.event.get():
        handle_mouse_or_keyboard_event(event, playerRect)


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


def handle_mouse_or_keyboard_event(event, playerRect):
    # global reverseCheat, slowCheat, score

    if event.type == QUIT:
        program_exit()

    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     if (event.button == 1):
    #         reverseCheat = True
    #     if (event.button == 3):
    #         slowCheat = True
    #
    # if event.type == pygame.MOUSEBUTTONUP:
    #     if (event.button == 1):
    #         reverseCheat = False
    #         score = score / 2
    #     if (event.button == 3):
    #         slowCheat = False
    #         score = score / 2
    #
    # if event.type == KEYDOWN:
    #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Mouse left click
    #         reverseCheat = True
    #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:  # Mouse right click
    #         slowCheat = True

    if event.type == KEYUP:
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Mouse left click
        #     reverseCheat = False
        #     score = 0
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:  # Mouse right click
        #     slowCheat = False
        #     score = 0
        if event.key == K_ESCAPE:
            program_exit()

    if event.type == MOUSEMOTION:
        # If the mouse moves, move the player where the cursor is.
        playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)


def program_exit():
    pygame.quit()
    sys.exit()

def add_new_animal(animals_list):
    # Add new animals at the top of the screen
    animalSize = random.randint(ANIMAL_MIN_SIZE, ANIMAL_MAX_SIZE)
    newAnimal = {
        'rect': build_rectangle_at_random_top_position(animalSize),
        'speed': random.randint(ANIMAL_MIN_SPEED, ANIMAL_MAX_SPEED),
        'surface': pygame.transform.scale(get_animal(), (animalSize, animalSize)),
    }
    animals_list.append(newAnimal)


def build_rectangle_at_random_top_position(animalSize):
    return pygame.Rect(random.randint(0, WINDOW_WIDTH - animalSize), 0 - animalSize, animalSize, animalSize)


def new_animal_is_needed():
    # Increase counter that indicates that new animals are needed
    global animalAddCounter
    # if not reverseCheat and not slowCheat:
    animalAddCounter += 1
    if animalAddCounter == ADD_NEW_ANIMAL_RATE:
        animalAddCounter = 0
        return True
    return False


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




def draw_black_game_window(windowSurface):
    # Draw the game world on the window.
    windowSurface.fill(BACKGROUND_COLOR)


def add_new_animal_if_needed():
    global newAnimalsNeeded
    newAnimalsNeeded = new_animal_is_needed()
    if newAnimalsNeeded:
        add_new_animal(animals)
        newAnimalsNeeded = False

score = 0

while True:
    # set up the start of the game
    animals = []
    # score = 0
    # reverseCheat = slowCheat = False
    animalAddCounter = 0
    newAnimalsNeeded = False

    while True:  # the game loop runs while the game part is playing

        score += 1  # increase score
        get_mouse_keyboard_events()
        add_new_animal_if_needed()

        # Move the mouse cursor to match the player.
        # pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)
        move_the_animals_down(animals)
        delete_fallen_animals(animals)
        draw_black_game_window(windowSurface)
        # draw_scores(windowSurface, score, topScore)
        # draw_player()
        draw_all_animals(animals)

        # update screen
        pygame.display.update()

        # Check if any of the animals have hit the player.
        # if player_has_hit_animal(playerRect, animals):
        #     if score > topScore:
        #         topScore = score  # set new top score
        #     draw_black_game_window(windowSurface)
        #     draw_player()
        #     draw_scores(windowSurface, score, topScore)
        #     pygame.display.update()
        #     wait_for_player_to_press_key()
        #     break

        mainClock.tick(FPS)
