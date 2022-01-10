from src import board
import pygame
import src.constants
import numpy as np
import sys
from src.board import Board, SelectionButton, RotateButton, ShipsText, Square


def create_ship_buttons(texts):
    four_button = SelectionButton(src.constants.FOUR_BUTTON, texts[0].x + 100, texts[0].y, True, False, src.constants.FOUR_HIGHLIGHT, 4)
    three_button = SelectionButton(src.constants.THREE_BUTTON, texts[1].x + 100, texts[1].y, True, False, src.constants.THREE_HIGHLIGHT, 3)
    two_button = SelectionButton(src.constants.TWO_BUTTON, texts[2].x + 100, texts[2].y, True, False, src.constants.TWO_HIGHLIGHT, 2)
    one_button = SelectionButton(src.constants.ONE_BUTTON, texts[3].x + 100, texts[3].y, True, False, src.constants.ONE_HIGHLIGHT, 1)
    return four_button, three_button, two_button, one_button


def create_text(board):
    x = board.board_pos[0]
    y = board.board_pos[1]
    text4 = ShipsText(1, x + 500, y)
    text3 = ShipsText(2, x + 500, y + 100)
    text2 = ShipsText(3, x + 500, y + 200)
    text1 = ShipsText(4, x + 500, y + 300)
    return text4, text3, text2, text1


def create_ships(board: Board):
    '''
    Creates Square objects representing ships in game. Each ship has a number assigned to it, so that
    the game knows what to draw on the board. Numbers from 1 to 4 are assigned to horizontal ships (eg. 1 means horizontal one-square ship).
    Numbers from 5 to 8 are assgined to vertical ships.
    '''
    one_h = Square(board.square_size, 1, 1)
    two_h = Square(board.square_size, 2, 1)
    three_h = Square(board.square_size, 3, 1)
    four_h = Square(board.square_size, 4, 1)

    one_v = Square(board.square_size, 1, 1)
    two_v = Square(board.square_size, 1, 2)
    three_v = Square(board.square_size, 1, 3)
    four_v = Square(board.square_size, 1, 4)

    return one_h, two_h, three_h, four_h, one_v, two_v, three_v, four_v

def draw_menu(screen, texts, board, selection_buttons):
    board.draw_board()
    screen.blit(board.surface, board.board_pos)
    for text in texts:
        text.draw(screen)
    for button in selection_buttons:
        button.draw(screen)



def main_board_creation(screen):
    screen.fill(src.constants.BACKGROUND)
    board = Board(src.constants.BOARD_SIZE, src.constants.BOARD_POS)
    texts = create_text(board)
    selection_buttons = create_ship_buttons(texts)
    ships = create_ships(board)
    run = True
    choice = 1
    while run:
        draw_menu(screen, texts, board, selection_buttons)
        ships[choice].update(board.board_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ships[choice].draw(board.surface)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                ships[choice].remove(board.surface)
        pygame.display.flip()