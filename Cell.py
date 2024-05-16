import pygame


class Cell:
    def __init__(self,x,y,alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.side = 10
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x,self.y,self.side,self.side)

    def display(self, screen):
        if self.alive:
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)
        pygame.draw.rect(
            screen,
            self.color,
            self.rect
        )