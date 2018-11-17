import pygame


#  Константи
FPS = 100                                       #   100 кадрів в секунду, або 1 кадр кожні 10 мілісекунд
WINDOW_COLOR_WHITE = (255, 255, 255)            #   білий колір, яким ми зафарбовуємо екран (в форматі RGB)
WINDOW_SIZE = (1000, 800)                       #   розміри вікна (розширення)

pygame.init()                                   #   початкові налаштування бібліотеки  pygame
display = pygame.display.set_mode(WINDOW_SIZE)  #   створити вікна програми з заданими розмірами
clock = pygame.time.Clock()                     #   створити годинник


class Panda:

    def __init__(self, image, x, y,  name):
        self.image = image
        self.name = name
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_another_panda_near_this_panda(self, other_panda):
        is_near = self.rect.colliderect(other_panda)
        if is_near:
            print("Панда ***" + self.name + "*** поряд з пандою  ***" + other_panda.name + "***!")

    def draw_panda_on_window(self, window):
        window.blit(self.image, self.rect)



def move_panda(panda, x, y, direction_text):
    print("Panda " + panda.name + " moved to: " + direction_text)
    panda.rect.x = panda.rect.x + x
    panda.rect.y = panda.rect.y + y

def create_panda(image_file, start_x, start_y, panda_name):
    print("Create panda: " + panda_name)
    image = pygame.image.load(image_file)
    panda = Panda(image, start_x, start_y, panda_name)

    return panda

def need_to_close_proram():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


#    events - key pressed
#
possible_keys = {
    pygame.K_LEFT:      {'x': -5,   'y': 0,   'key_name': 'LEFT'},
    pygame.K_RIGHT:     {'x': +5,   'y': 0,   'key_name': 'RIGHT'},
    pygame.K_UP:        {'x': 0,    'y': -5,  'key_name': 'UP'},
    pygame.K_DOWN:      {'x': 0,    'y': 5,   'key_name': 'DOWN'}
}

#   move panda if needed
#
def move_panda_if_needed_2(panda):
    for key in possible_keys:
        if(key_is_pressed(key)):
            x_diff = possible_keys.get(key).get('x')
            y_diff = possible_keys[key].get('y')
            key_name = possible_keys[key]['str']
            move_panda(panda, x_diff, y_diff, key_name)

# check, if key is pressed
#
def key_is_pressed(key):
    all_pressed_keys = pygame.key.get_pressed()
    return all_pressed_keys[key] != 0



def move_panda_if_needed(panda):
    all_pressed_keys = pygame.key.get_pressed()

    if all_pressed_keys[pygame.K_LEFT]:
        move_panda(panda, -5, 0, "LEFT")

    if all_pressed_keys[pygame.K_RIGHT]:
        move_panda(panda, +5, 0, "RIGHT")

    if all_pressed_keys[pygame.K_UP]:
        move_panda(panda, 0, -5, "UP")

    if all_pressed_keys[pygame.K_DOWN]:
        move_panda(panda, 0, +5, "DOWN")


panda1 = create_panda('panda.jpg', 100, 100, "Перша панда")
panda2 = create_panda('panda.jpg', 100, 100, "Друга панда")
panda1.draw_panda_on_window(display)
panda2.draw_panda_on_window(display)

running = True

while running:
    move_panda_if_needed_2(panda1)
    display.fill(WINDOW_COLOR_WHITE)                        #   намалювати білий екран
    panda1.draw_panda_on_window(display)                    #   панда 1 сама себе малює на екрані
    panda2.draw_panda_on_window(display)                    #   панда 2 сама себе малює на екрані
    panda1.check_another_panda_near_this_panda(panda2)
    pygame.display.update()                                 #   оновити екран
    running = not need_to_close_proram()                    #   індикатор завершення програми (використовується в циклі while)

    clock.tick(FPS)
