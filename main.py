import pygame
from Cons.board import Board
from Cons.Constants import HEIGHT, WIDTH, SQUARE_SIZE
from Cons.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checker game with AI')
FPS = 60
board = Board()

def get_pos_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_mouse(pos)
                piece = board.get_piece(row, col)
                board.move_piece(piece, 4, 3)

        game.update()

    pygame.quit()

main()