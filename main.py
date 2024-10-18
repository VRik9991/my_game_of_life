import pygame
from CellManager import CellManager
from Figure import Figure
import utils
from FigureManager import FigureManager
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.init()

c = CellManager()
f = FigureManager()

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
                f.add_figure(posX, posY, c)
            if event.button == pygame.BUTTON_WHEELUP:
                f.chosen_figure_number += 1

                if f.chosen_figure_number >= len(f.figures):
                    f.chosen_figure_number = 0
            if event.button == pygame.BUTTON_WHEELDOWN:
                f.chosen_figure_number -= 1

                if f.chosen_figure_number < 0:
                    f.chosen_figure_number = len(f.figures) - 1

    c.display(screen)
    pygame.display.flip()
    clock.tick(15)
    # if pygame.mouse.get_pressed(5)[0]:
    #     c.click_to_live()
    if not pause:
        c.live_or_dead()
        screen.fill((0, 0, 0))
