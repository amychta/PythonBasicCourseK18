import pygame


FPS = 100
COLOR_WHITE = (255, 255, 255)
WINDOW_SIZE = (1000, 800)
panda_image_cosmos = pygame.image.load('panda.jpg')
panda_image_happy = pygame.image.load('panda_happy.jpg')
pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)


class Panda:
    def __init__(self, x, y):
        self.image = panda_image_cosmos
        self.rectangle = self.image.get_rect()
        self.rectangle.x = x
        self.rectangle.y = y

    def change_skin_if_another_panda_is_near(self, other_panda):
        is_near = self.rectangle.colliderect(other_panda.rectangle)

        if is_near:
            print("Another panda is near me!")
            self.image = panda_image_happy
        else:
            self.image = panda_image_cosmos

    def draw_panda_on_window(self, window):
        window.blit(self.image, self.rectangle)


    def move(self, x_diff, y_diff, direction_text):
        print("Panda is moved to: " + direction_text)
        self.rectangle.x = self.rectangle.x + x_diff
        self.rectangle.y = self.rectangle.y + y_diff


def need_to_close_proram():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def move_panda_if_needed(panda):
    all_pressed_keys = pygame.key.get_pressed()

    if all_pressed_keys[pygame.K_LEFT]:
        panda.move(-5, 0, "LEFT")

    if all_pressed_keys[pygame.K_RIGHT]:
        panda.move(+5, 0, "RIGHT")

    if all_pressed_keys[pygame.K_UP]:
        panda.move(0, -5, "UP")

    if all_pressed_keys[pygame.K_DOWN]:
        panda.move(0, +5, "DOWN")


panda1 = Panda(300, 500)
panda2 = Panda(100, 200)
running = True

while running:
    move_panda_if_needed(panda1)
    window.fill(COLOR_WHITE)
    panda1.change_skin_if_another_panda_is_near(panda2)
    panda2.draw_panda_on_window(window)
    panda1.draw_panda_on_window(window)
    pygame.display.update()
    running = not need_to_close_proram()

