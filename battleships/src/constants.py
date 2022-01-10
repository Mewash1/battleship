import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 1072, 603
BACKGROUND = 242, 216, 186
BLACK = 0, 0, 0
FONT = pygame.font.SysFont('calibri', 32)
CLOCK = pygame.time.Clock()
BATTLESHIP = "battleships/data/battleships.jpg"
BOARD_SIZE = (350, 350)
FIRST_BOARD_POS = (200, HEIGHT/2 - BOARD_SIZE[0]/2)
TEXT_POS = (700, HEIGHT/2 - BOARD_SIZE[0]/2)