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
        for coordinate in self.cell_coordinates:
            x1, y1 = coordinate
            cell_manager.cells[y + y1][x + x1].alive = True


f = Figure('figures/glider.json')
