from constants import CELL_SIDE


def get_cell_coordinates(posX, posY):
    posX = posX // CELL_SIDE * CELL_SIDE
    posY = posY // CELL_SIDE * CELL_SIDE

    return int(posX/CELL_SIDE), int(posY/CELL_SIDE)
