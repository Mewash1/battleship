import pygame
import constants


class Board:
    def __init__(self, board_size, board_pos, screen_w, screen_h) -> None:
        self.board_size = board_size
        self.surface = pygame.Surface(board_size)
        self.board_pos = board_pos
        self.screen_w = screen_w
        self.screen_h = screen_h
    
    def draw_board(self):
        square_size = self.screen_w // 10 
        for i in range(0, self.screen_w + 1, square_size):
            x, y = i, i
            pygame.draw.line(self.surface, (255, 255, 255), (x, 0), (x, self.screen_w), 4)
            pygame.draw.line(self.surface, (255, 255, 255), (0, y), (self.screen_w, y), 4)

    def draw_ship(self, ship_type):
        


class Menu:
    pass


class Cube:
    def update(self, sizebtwn):
        x, y = pygame.mouse.get_pos()
        x, y = x - constants.FIRST_BOARD_POS[0], y - constants.FIRST_BOARD_POS[1]
        ix = x // sizebtwn
        iy = y // sizebtwn
        self.cx, self.cy = ix * sizebtwn, iy * sizebtwn
        self.square = pygame.Rect(self.cx, self.cy, sizebtwn, sizebtwn)
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.square)
    def draw_at_point(self, surface, point):
        pygame.draw.rect(surface, (255, 255, 255), point)
    def remove(self, surface):
        pygame.draw.rect(surface, constants.BACKGROUND, self.square)
    
