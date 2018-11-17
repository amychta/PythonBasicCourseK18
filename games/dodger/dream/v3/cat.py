import pygame

# --- constants --- (UPPER_CASE_NAMES)

FPS = 100
WHITE = (255, 255, 255)

# --- classes --- (CamelCaseNames)

class Cat:

    def __init__(self, x, y):
        self.img = pygame.image.load('icons\panda.jpg')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.img, self.rect)

    def colide(self, other_sprite):
        col = self.rect.colliderect(other_sprite)
        if col:
            print("crash!")

# --- main --- (lower_case_names)

# - init -

pygame.init()

display_surf = pygame.display.set_mode((800, 800)) # full is 1900, 1000
pygame.display.set_caption('Animation')

# - objects -

cat1 = Cat(10, 10)
cat2 = Cat(100, 100)

# - mainloop -

fps_clock = pygame.time.Clock()
running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        cat1.rect.y -= 3
    if keys[pygame.K_DOWN]:
        cat1.rect.y += 3
    if keys[pygame.K_LEFT]:
        cat1.rect.x -= 3
    if keys[pygame.K_RIGHT]:
        cat1.rect.x += 3

    # - updates (without draws) -

    cat1.colide(cat2)

    # - draws (without updates) -

    display_surf.fill(WHITE)
    cat1.draw(display_surf)
    cat2.draw(display_surf)

    pygame.display.update()

    fps_clock.tick(FPS)

# - end -

pygame.quit()