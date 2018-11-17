import pygame

pygame.init()
display = pygame.display.set_mode((1000, 800))

FPS = 100
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

while True:
    display.fill(WHITE)
    pygame.display.update()
    clock.tick(FPS)


    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        print("pressed key up")
