import pygame
from Cell import Cell
import utils
from constants import CELLS_IN_COLUMN, CELLS_IN_ROW, CELL_SIDE


class CellManager:
    def __init__(self):
        self.cells: list[list[Cell]] = []
        live = False
        posY = 0
        posX = 0
        self.empty_field = []
        for i in range(CELLS_IN_COLUMN):
            self.cells.append([])
            for j in range(CELLS_IN_ROW):
                self.cells[-1].append(Cell(posX, posY, live))
                # live = not live
                posX += CELL_SIDE
            # live = not live
            posX = 0
            posY += CELL_SIDE
        # self.cells[30][40].alive = True
        # self.cells[30][42].alive = True
        # self.cells[29][42].alive = True
        # self.cells[28][44].alive = True
        # self.cells[27][44].alive = True
        # self.cells[26][44].alive = True
        # self.cells[26][46].alive = True
        # self.cells[26][47].alive = True
        # self.cells[25][46].alive = True
        # self.cells[27][46].alive = True

    def display(self, screen):
        for i in range(CELLS_IN_COLUMN):
            for j in range(CELLS_IN_ROW):
                self.cells[i][j].display(screen)

    def count_living_neighbours(self, x, y):
        count = 0
        start_x = -1
        end_x = 2
        start_y = -1
        end_y = 2
        if y == 0:
            start_y += 1
        if y == CELLS_IN_COLUMN - 1:
            end_y -= 1
        if x == 0:
            start_x += 1
        if x == CELLS_IN_ROW - 1:
            end_x -= 1
        for i in range(start_y, end_y):
            for j in range(start_x, end_x):
                if self.cells[y + i][x + j].alive and not (i == 0 and j == 0):
                    count += 1
        return count

    def live_or_dead(self):
        generation = []
        posY = 0
        posX = 0
        for i in range(CELLS_IN_COLUMN):
            generation.append([])
            for j in range(CELLS_IN_ROW):
                generation[-1].append(Cell(posX, posY, False))
                posX += CELL_SIDE
            posX = 0
            posY += CELL_SIDE
        for i in range(CELLS_IN_COLUMN):
            for j in range(CELLS_IN_ROW):
                living_neighbours = self.count_living_neighbours(j, i)
                if living_neighbours < 2:
                    generation[i][j].alive = False
                if living_neighbours == 2:
                    generation[i][j].alive = self.cells[i][j].alive
                if living_neighbours == 3:
                    generation[i][j].alive = True
                if living_neighbours > 3:
                    generation[i][j].alive = False
        self.cells = generation.copy()

    def click_to_live(self):
        posX, posY = pygame.mouse.get_pos()
        posX, posY = utils.get_cell_coordinates(posX, posY)
        if -1 < posX < CELLS_IN_ROW and -1 < posY < CELLS_IN_COLUMN:
            self.cells[int(posY)][int(posX)].alive = not self.cells[int(posY)][int(posX)].alive

    def clear(self):
        posX = 0
        posY = 0
        self.cells = []
        for i in range(CELLS_IN_COLUMN):
            self.cells.append([])
            for j in range(CELLS_IN_ROW):
                self.cells[-1].append(Cell(posX, posY, False))
                # live = not live
                posX += CELL_SIDE
            # live = not live
            posX = 0
            posY += CELL_SIDE
