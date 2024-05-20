def get_cell_coordinates(posX, posY):
    posX = posX // 10 * 10
    posY = posY // 10 * 10
    return int(posX/10), int(posY/10)
