import pygame
import json
import utils

from CellManager import CellManager


class Figure:
    def __init__(self, filename):
        with open(filename, encoding='utf-8') as file:
            data = json.loads(''.join(file.readlines()))
        self.name = data['name']
        self.cell_coordinates = data['coordinates']

    def add_figure(self, x, y, cell_manager: CellManager):
        end_x = 0
        end_y = 0
        for coordinates in self.cell_coordinates:
            if end_y < coordinates[1]:
                end_y = coordinates[1]
            if end_x < coordinates[0]:
                end_x = coordinates[0]

            for i in range(y, y + end_y + 1):
                for j in range(x, x + end_x + 1):
                    if 0 < i  < 60 and 0 < j < 80:
                        cell_manager.cells[i][j].alive = False
        for coordinate in self.cell_coordinates:
            x1, y1 = coordinate
            if 0 < y + y1 < 60 and 0 < x + x1 < 80:
                cell_manager.cells[y + y1][x + x1].alive = True
