import pygame

pygame.init()
display = pygame.display.set_mode((1000, 800))

FPS = 100
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
running = True



class Panda:


    def __init__(self, x, y):
        self.img = pygame.image.load('panda.jpg')
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

panda1 = Panda(100, 200)
panda2 = Panda(10, 50)
panda3 = Panda(100, 200)



panda4 = Panda(100, 200)

while running:
    display.fill(WHITE)
    panda4.draw(display)
    pygame.display.update()
    clock.tick(FPS) # 10 millisecond

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        print("pressed key: UP")
