import pygame
from .Constants import WHITE, BLACK, GREY, BLUE, SQUARE_SIZE, CROWN

class Piece:
    PADDING = 18
    OUTLINE = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1

    def draw_self(self, window):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y), radius+self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if True:
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def make_king(self):
        self.king = True

    def calc_pos(self):
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2

    def move(self, col, row):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(('P'))



