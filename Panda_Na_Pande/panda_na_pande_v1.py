import pygame

# Гра  ПАНДА НА ПАНДІ
# суть гри: керувати однією з панд. Коли одна панда буде над іншою - одну з них зробити веселою
# Програма відслідковує події: натискання на кнопки вгору, вниз, вліво, вправо. І закриття вікна, натискаючи на хрестик
#
# Алгоритм:
#
# 1. Створити вікно, на якому будемо малювати
# 1. Створити 2 панди. Одна буде нерухома, а іншою будемо керувати
#
# 2. В безкінечному циклі
#      2.1  Відслідковувати кнопку, яку натиснули. Змінити координати панди-1, якщо потрібно
#      2.1  Залити екран білим кольором
#      2.1  Якщо панди накладаються, то змінити картинку панди-1 на веселу. Інакше використати картинку панди-в-космосі
#      2.1  Оновити екран програми
#      2.1  Скинути флаг і завершити програму, якщо користувач закриває вікно програми
#

#  Константи
FPS = 100                                               #   100 кадрів в секунду, або 1 кадр кожні 10 мілісекунд
COLOR_WHITE = (255, 255, 255)                           #   білий колір, яким ми зафарбовуємо екран (в форматі RGB)
WINDOW_SIZE = (1000, 800)                               #   розміри вікна (розширення)
panda_image_cosmos = pygame.image.load('panda.jpg')     #   картинка, бажано розміром не більше 200 * 200
panda_image_happy = pygame.image.load('panda_happy.jpg')

# Початкові налаштування
pygame.init()                                       #   початкові налаштування бібліотеки  pygame
window = pygame.display.set_mode(WINDOW_SIZE)       #   створити вікна програми з заданими розмірами
# clock = pygame.time.Clock()                       #   створити годинник


# У панди є властивості (характеристики, поля) і поведінка (методи)
# Властивості:
# image - картинка панди
# rectangle - квадрат навколо картинки панди
# цей квадрат навколо панди теж має характеристики: координати по ширині (x) та по висоті (y)
class Panda:
    # Ця функція викликається при створенні панди.
    # x та y - це початкові координати панди
    # створити панду з такими параметрами: картинка панди, координати x та y, ім'я панди
    def __init__(self, x, y):
        self.image = panda_image_cosmos                              #   прямокутник навколо картинки
        self.rectangle = self.image.get_rect()                  #   прямокутник навколо картинки
        self.rectangle.x = x                                    #   початкова координата по ширині
        self.rectangle.y = y                                    #   початкова координата по висоті


    # вивести повідомлення, якщо інша панда поряд
    def change_skin_if_another_panda_is_near(self, other_panda):
        is_near = self.rectangle.colliderect(other_panda.rectangle) #  colliderect - це вбудована функція бібліотеки pygame
                                                                    #  вона перевіряє, що прямокутники навколо двох панд накладаються один на інший
        if is_near:
            print("Another panda is near me!")
            self.image = panda_image_happy       # якщо поряд інша панда, то використати картинку веселої панди
        else:
            self.image = panda_image_cosmos      # інакше використати картинку панди в космосі

    # намалювати панду на вікні
    def draw_panda_on_window(self, window):
        window.blit(self.image, self.rectangle)     # функція blit - вбудована функція бібліотеки pygame
                                                    # малює картинку панди на вікні

    # змінити координати панди
    def move(self, x_diff, y_diff, direction_text):
        print("Panda is moved to: " + direction_text)
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
#
def move_panda_if_needed(panda):
    # all_pressed_keys - це список, з якого можна визначити, яка кнопка клавіатури натиснута
    all_pressed_keys = pygame.key.get_pressed()

    if all_pressed_keys[pygame.K_LEFT]:
        panda.move(-5, 0, "LEFT")

    if all_pressed_keys[pygame.K_RIGHT]:
        panda.move(+5, 0, "RIGHT")

    if all_pressed_keys[pygame.K_UP]:
        panda.move(0, -5, "UP")

    if all_pressed_keys[pygame.K_DOWN]:
        panda.move(0, +5, "DOWN")


panda1 = Panda(300, 500)                                    #   створили панду, яка буде рухатися
panda2 = Panda(100, 200)                                    #   панда, яка стоятиме на місці
running = True                                              #   індикатор завершення програми

while running:

    move_panda_if_needed(panda1)                            #   перемістити панду 1, якщо натиснуті кнопки вниз вверз вліво вправо

    # перемалювари повністю вікно
    window.fill(COLOR_WHITE)                                #   намалювати білий екран
    panda1.change_skin_if_another_panda_is_near(panda2)     #   змінити картинку в залежності від того, чи поряд інша панда
    panda2.draw_panda_on_window(window)                     #   намалювати панду 2
    panda1.draw_panda_on_window(window)                     #   намалювати панду 1
    pygame.display.update()                                 #   оновити екран

    running = not need_to_close_proram()                    #   індикатор завершення програми (використовується в циклі while)

    # clock.tick(FPS)                                         #   почекати 10 мілісекунд
