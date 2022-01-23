from battleships.src.second_screen import (
    check_draw_submit,
    use_rotation
)
from battleships.src.create_objects import create_rotate_button, create_text
from battleships.src.classes.Board import Board
import pygame


def test_check_draw_submit():
    board = Board((10, 10), (0, 0))
    texts = create_text(board)
    assert check_draw_submit(texts) is False
    for text in texts:
        text.update(0)
    assert check_draw_submit(texts) is True


def test_use_rotation():
    screen = pygame.display.set_mode((10, 10))
    board = Board((10, 10), (0, 0))
    rotate_button = create_rotate_button(board)
    choice = 1
    choice = use_rotation(rotate_button, choice)
    assert choice == 5
    choice = use_rotation(rotate_button, choice)
    assert choice == 1
