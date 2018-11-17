import pygame


#  Константи
FPS = 100                                       #   100 кадрів в секунду, або 1 кадр кожні 10 мілісекунд
WINDOW_COLOR_WHITE = (255, 255, 255)            #   білий колір, яким ми зафарбовуємо екран (в форматі RGB)
WINDOW_SIZE = (1000, 800)                       #   розміри вікна (розширення)

pygame.init()                                   #   початкові налаштування бібліотеки  pygame
display = pygame.display.set_mode(WINDOW_SIZE)  #   створити вікна програми з заданими розмірами
clock = pygame.time.Clock()                     #   створити годинник


# Клас  ПАНДА. Кожна панда має властивості, і дії, які вона може робити
#
#   Властивості(характеристики):
#
#   x - координата по x
#   y - координата по y
#   image - картинка панди
#   name - ім'я панди
#
#   Дії (функції)
#
#   Намалювати себе на екрані
#   __init__    - функція викликається при створенні панди (конструктор)
#   draw        - намалювати себе на екрані
#   colide        - перевірити, чи перетинаємся з іншими пандами



class Panda:

    # Ця функція виконується, коли програма бачить строчку типу:
    #       panda1 = Panda('panda.jpg', 100, 500, "Панда з Африки")
    #
    #   image -- назва файлу з картинкою
    #   x -- початкова координата панди - по висот (в діапазоні від 0 до 800. Висота 800 задається в константі WINDOW_SIZE)
    #   y -- початкова координата панди (в діапазоні від 0 до 1000. Ширина 1000 задається в константі WINDOW_SIZE)
    #   y -- назва картинки
    #   name -- назва картинки
    #


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
    move_panda_if_needed(panda1)
    display.fill(WINDOW_COLOR_WHITE)                        #   намалювати білий екран
    panda1.draw_panda_on_window(display)                    #   панда 1 сама себе малює на екрані
    panda2.draw_panda_on_window(display)                    #   панда 2 сама себе малює на екрані
    panda1.check_another_panda_near_this_panda(panda2)
    pygame.display.update()                                 #   оновити екран
    running = not need_to_close_proram()                    #   індикатор завершення програми (використовується в циклі while)

    clock.tick(FPS)
