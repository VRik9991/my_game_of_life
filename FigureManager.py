import json

from CellManager import CellManager
from Figure import Figure
import os


class FigureManager:
    def __init__(self):
        self.figures = []
        self.chosen_figure_number = 0
        for file_name in os.listdir('figures'):
            self.figures.append(Figure("figures/" + file_name))

    def add_figure(self, x, y, cell_manager: CellManager):
        self.figures[self.chosen_figure_number].add_figure(x, y, cell_manager)
