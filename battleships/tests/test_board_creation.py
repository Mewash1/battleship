from src.board import Board
from src.board_creation import create_ship_buttons, create_text
import src.constants
import pygame


def test_create_ship_buttons():
    screen = pygame.display.set_mode(src.constants.SIZE)
    board = Board(src.constants.BOARD_SIZE, src.constants.BOARD_POS)
    texts = create_text(board)
    selection_buttons = create_ship_buttons(texts)
    assert selection_buttons[0].x == board.x + 500