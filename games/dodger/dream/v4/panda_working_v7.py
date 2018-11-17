import pygame


#  Константи
FPS = 100                                           #   100 кадрів в секунду, або 1 кадр кожні 10 мілісекунд
WINDOW_BACKGROUND_COLOR_WHITE = (255, 255, 255)     #   білий колір, яким ми зафарбовуємо екран (в форматі RGB)
WINDOW_SIZE = (1000, 800)                           #   розміри вікна (розширення)
pygame.init()                                       #   початкові налаштування бібліотеки  pygame
window = pygame.display.set_mode(WINDOW_SIZE)       #   створити вікна програми з заданими розмірами
clock = pygame.time.Clock()                         #   створити годинник

panda__cosmos = pygame.image.load('panda.jpg')
panda__happy = pygame.image.load('panda_happy.png')


class Panda:
    # створити панду з такими параметрами: картинка панди, координати x та y, ім'я панди
    def __init__(self, start_x, start_y, panda_name):
        self.image = panda__cosmos                              #   прямокутник навколо картинки
        self.rectangle = self.image.get_rect()                  # прямокутник навколо картинки
        self.rectangle.x = start_x                              #   початкова координата по ширині
        self.rectangle.y = start_y                              #   початкова координата по висоті
        self.name = panda_name                                  #   ім'я панди
        print("Panda " + panda_name + " created")

    # вивести повідомлення, якщо інша панда поряд
    def change_skin_if_another_panda_is_near(self, other_panda):
        is_near = self.rectangle.colliderect(other_panda.rectangle) #  colliderect - це вбудована функція бібліотеки pygame
                                                                    #  вона перевіряє, що прямокутники навколо двох панд накладаються один на інший
        if is_near:
            print("I am panda " + self.name + ". Another panda " + other_panda.name + " is near me!")
            self.image = panda__happy       # якщо поряд інша панда, то використати картинку веселої панди
        else:
            self.image = panda__cosmos      # інакше використати панди в космосі

    # намалювати панду на вікні
    def draw_panda_on_window(self):
        global window
        window.blit(self.image, self.rectangle)     # функція blit - вбудована функція бібліотеки pygame

    # змінити координати панди
    def move(self, x_diff, y_diff, direction_text):
        print("Panda " + self.name + " is moved to: " + direction_text)
        self.rectangle.x = self.rectangle.x + x_diff
        self.rectangle.y = self.rectangle.y + y_diff


# Перевірити, чи треба завершити програму
# Подія pygame.QUIT відбудеться, якщо натиснути на хрестик закриття вікна програми
def need_to_close_proram():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

# функція яка перевіряє усі натиснуті кнопки і відповідно рухає панду
# в параметрах координат вказано, на скільки змінити координати панди по висоті, по ширині і як ця операція буде називатися
#
def move_panda_if_needed(panda):
    all_pressed_keys = pygame.key.get_pressed()

    if all_pressed_keys[pygame.K_LEFT]:
        panda.move(-10, 0, "LEFT")

    if all_pressed_keys[pygame.K_RIGHT]:
        panda.move(+10, 0, "RIGHT")

    if all_pressed_keys[pygame.K_UP]:
        panda.move(0, -10, "UP")

    if all_pressed_keys[pygame.K_DOWN]:
        panda.move(0, +10, "DOWN")


panda1 = Panda(100, 100, "Перша панда")
panda2 = Panda(100, 100, "Друга панда")
running = True                                             #   флаг завершення програми

while running:

    move_panda_if_needed(panda1)                            #   перемістити панду 1, якщо натиснуті кнопки вниз вверз вліво вправо

    # перемалювари повністю вікно
    window.fill(WINDOW_BACKGROUND_COLOR_WHITE)              #   намалювати білий екран
    panda1.draw_panda_on_window()                           #   намалювати панду 1
    panda2.draw_panda_on_window()                           #   намалювати панду 2
    pygame.display.update()                                 #   оновити екран
    panda1.change_skin_if_another_panda_is_near(panda2)     #   змінити картинку в залежності від того, чи поряд інша панда

    running = not need_to_close_proram()                    #   індикатор завершення програми (використовується в циклі while)

    clock.tick(FPS)                                         #   почекати 10 мілісекунд
