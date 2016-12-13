import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONUP
from lib import Board

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init(48000, -16, 1, 1024)  # Avoid noise when starting the game
board = Board(grid_size=3, box_size=100, border=50, line_width=10)

if __name__ == "__main__":
    """
    TicTacToe Main Function
    Start the TicTactoe Game. Stop when user click the Exit button
    """
    board.display_start_screen()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                x, y = event.pos
                board.process_click(x, y)

        pygame.display.update()
        clock.tick(30)
