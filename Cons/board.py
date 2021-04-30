import pygame
from .Constants import BLACK, WHITE, CYAN, SQUARE_SIZE, ROWS, COLS, BLUE
from .pieces import Piece

class Board:
    def __init__(self):
        self.board = []
        self.black = self.blue = 12
        self.black_king = self.blue_king = 0
        self.create_board()

    def move_piece(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS or row == 0:
            piece.make_king()
            if piece.col == BLACK:
                self.black_king += 1
            else:
                self.blue_king += 1


    def get_piece(self, row, col):
        return self.board[row][col]

    def draw_squares(self, window):
        window.fill(CYAN)
        for rows in range(ROWS):
            for cols in range(rows % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, (rows*SQUARE_SIZE, cols*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)



    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_self(window)