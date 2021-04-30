import pygame
from .Constants import BLACK, BLUE
from .board import Board


class Game:
    def __init__(self, window):
        self.turn = BLACK
        self.selected = None
        self.board = Board()
        self.valid_moves = {}
        self.window = window

    def update(self):
        self.board.draw(self.window)
        pygame.display.update()

