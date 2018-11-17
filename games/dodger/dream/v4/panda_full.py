import pygame

# --- constants ---

FPS = 100
WHITE = (255, 255, 255)

# --- images ---

class Panda:


    def __init__(self, x, y):
        self.img = pygame.image.load('icons\panda.jpg')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        # img = pygame.image.load('icons\panda.jpg')
        surface.blit(self.img, self.rect)

    def colide(self, other_sprite):
        col = self.rect.colliderect(other_sprite)
        if col:
            print("Панди поряд!")

# --- main --- (lower_case_names)
# - init -

pygame.init()
display_surf = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Animation')

panda1 = Panda(10, 10)
panda2 = Panda(100, 100)

fps_clock = pygame.time.Clock()
running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        panda1.rect.y -= 3
    if keys[pygame.K_DOWN]:
        panda1.rect.y += 3
    if keys[pygame.K_LEFT]:
        panda1.rect.x -= 3
    if keys[pygame.K_RIGHT]:
        panda1.rect.x += 3

    # - updates (without draws) -

    panda1.colide(panda2)

    # - draws (without updates) -

    display_surf.fill(WHITE)
    panda1.draw(display_surf)
    panda2.draw(display_surf)

    pygame.display.update()

    fps_clock.tick(FPS)

# - end -

pygame.quit()