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


def create_ships(board: Board, choice):
    '''
    Creates Square objects representing ships in game. Each ship has a number assigned to it, so that
    the game knows what to draw on the board. Numbers from 1 to 4 are assigned to horizontal ships (eg. 1 means horizontal one-square ship).
    Numbers from 5 to 8 are assgined to vertical ships.
    '''
    if choice == 1:
        return Square(board.square_size, 1, 1)
    if choice == 2:
        return Square(board.square_size, 2, 1)
    if choice == 3:
        return Square(board.square_size, 3, 1)
    if choice == 4:
        return Square(board.square_size, 4, 1)
    if choice == 5:
        return Square(board.square_size, 1, 1)
    if choice == 6:
        return Square(board.square_size, 1, 2)
    if choice == 7:
        return Square(board.square_size, 1, 3)
    if choice == 8:
        return Square(board.square_size, 1, 4)
    
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
    '''

def draw_menu(screen, texts, board, selection_buttons):
    board.draw_board()
    screen.blit(board.surface, board.board_pos)
    for text in texts:
        text.draw(screen)
    for button in selection_buttons:
        button.draw(screen)


def update(board_pos, board_size, square_size):
    x, y = pygame.mouse.get_pos()
    x, y = x - board_pos[0], y - board_pos[1]
    ix = x // square_size
    iy = y // square_size
    cx, cy = ix * square_size, iy * square_size
    return int(cx/(board_size[0]//10)), int(cy/(board_size[0]//10)), cx, cy


def check_for_ships_around_point(cy, cx, array):
    print(cx, cy)
    if array[cx][cy] != 0:
        return False
    try:
        if array[cx - 1][cy] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cx + 1][cy] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cx][cy - 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cx][cy + 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cx - 1][cy - 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cx + 1][cy + 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cx - 1][cy + 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cx + 1][cy - 1] != 0:
            return False
    except IndexError:
        pass
    return True

    


def check_good_ship_placement(choice, cx, cy, array):
    if choice in {1, 2, 3, 4}:
        for y in range(choice):
            if not check_for_ships_around_point(cx, cy + y, array):
                return False
    elif choice in {5, 6, 7, 8}:
        for x in range(choice - 4):
            if not check_for_ships_around_point(cx + x, cy, array):
                return False
    return True




def check_length(choice, array, cy, cx):
    if choice == 1 or choice == 5:
        return True
    else:
        if choice in {2, 3, 4}:
            for x in range(choice):
                try:
                    if array[cx][cy + x] != 0:
                        return False
                except IndexError:
                    return False
        elif choice in {6, 7, 8}:
            for y in range(choice - 4):
                try:
                    if array[cx + y][cy] != 0:
                        return False
                except IndexError:
                    return False
        return True


def draw_ship(choice, cy, cx, array, surface, square_size, ix, iy):
    choice_dict = {
        1: (1, 1),
        2: (2, 1),
        3: (3, 1),
        4: (4, 1),
        5: (1, 1),
        6: (1, 2),
        7: (1, 3),
        8: (1, 4)
    }
    height = square_size * choice_dict[choice][0]
    width = square_size * choice_dict[choice][1]
    new_ship = pygame.Rect(ix, iy, height, width)
    pygame.draw.rect(surface, (255, 255, 255), new_ship)

    if choice > 4:
        for y in range(choice - 4):
            array[cx + y][cy] = 1
    else:
        for x in range(choice):
            array[cx][cy + x] = 1


def main_board_creation(screen):
    screen.fill(src.constants.BACKGROUND)
    board = Board(src.constants.BOARD_SIZE, src.constants.BOARD_POS)
    texts = create_text(board)
    selection_buttons = create_ship_buttons(texts)
    ships = []
    array = np.zeros((10, 10), dtype=int)
    run = True
    choice = 2
    while run:
        draw_menu(screen, texts, board, selection_buttons)
        cy, cx, ix, iy = update(board.board_pos, board.board_size, board.square_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (cy >= 0 and cy <= 9) and (cx >= 0 and cx <= 9):
                    if check_good_ship_placement(choice, cy, cx, array):
                        draw_ship(choice, cy, cx, array, board.surface, board.square_size, ix, iy)
                        print(array)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pass
        pygame.display.flip()