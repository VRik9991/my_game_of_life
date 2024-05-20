import pygame
from CellManager import CellManager
from Figure import Figure
import utils


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.init()

c = CellManager()
f = Figure('figures/glider.json')


running = True
pause = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                c.clear()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                c.click_to_live()
            if event.button == pygame.BUTTON_RIGHT:
                posX, posY = pygame.mouse.get_pos()
                posX, posY = utils.get_cell_coordinates(posX, posY)
                f.add_figure(posX,posY, c)
    c.display(screen)
    pygame.display.flip()
    clock.tick(15)
    if not pause:
        c.live_or_dead()
        screen.fill((0, 0, 0))
