import pygame
from CellManager import CellManager

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.init()

c = CellManager()

running = True
pause = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        if event.type == pygame.MOUSEBUTTONDOWN:
            c.click_to_live()
    c.display(screen)
    pygame.display.flip()
    clock.tick(15)
    if not pause:
        c.live_or_dead()
        screen.fill((0, 0, 0))



