import pygame
from ..constants import BACKGROUND


class Board:
    def __init__(self, board_size, board_pos) -> None:
        self.board_size = board_size
        self.surface = pygame.Surface(board_size)
        self.surface.fill(BACKGROUND)
        self.board_pos = board_pos
        self.square_size = self.board_size[0] // 10
    
    def draw_board(self):
        for i in range(0, self.board_size[0] + 1, self.square_size):
            x, y = i, i
            pygame.draw.line(self.surface, (255, 255, 255), (x, 0), (x, self.board_size[0]), 4)
            pygame.draw.line(self.surface, (255, 255, 255), (0, y), (self.board_size[0], y), 4)

    def draw_ship(self, ship_type):
        ship_type.draw()
