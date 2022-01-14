import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 1072, 603
BACKGROUND = 242, 216, 186
BLACK = 0, 0, 0
FONT = pygame.font.SysFont('calibri', 32)
CLOCK = pygame.time.Clock()
BATTLESHIP = "battleships/data/battleships.jpg"
BOARD_SIZE = (350, 350)
BOARD_POS = (200, HEIGHT/2 - BOARD_SIZE[0]/2)
TEXT_POS = (700, HEIGHT/2 - BOARD_SIZE[0]/2)
FOUR_BUTTON = "battleships/data/four_square.jpg"
THREE_BUTTON = "battleships/data/three_square.jpg"
TWO_BUTTON = "battleships/data/two_square.jpg"
ONE_BUTTON = "battleships/data/one_square.jpg"
FOUR_HIGHLIGHT = "battleships/data/four_highlight.jpg"
THREE_HIGHLIGHT = "battleships/data/three_highlight.jpg"
TWO_HIGHLIGHT = "battleships/data/two_highlight.jpg"
ONE_HIGHLIGHT = "battleships/data/one_highlight.jpg"
