from ast import Index
from src import board
import pygame
import src.constants
import numpy as np
import sys
from src.board import Board, SelectionButton, RotateButton, ShipsText, Square
from src.check_placement import check_good_ship_placement, check_length


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
    grid_x = x // square_size
    grid_y = y // square_size
    cx, cy = grid_x * square_size, grid_y * square_size
    return int(cx/(board_size[0]//10)), int(cy/(board_size[0]//10)), cx, cy


def draw_ship(choice, cx, cy, array, surface, square_size, grid_x, grid_y):
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
    new_ship = pygame.Rect(grid_x, grid_y, height, width)
    pygame.draw.rect(surface, (255, 255, 255), new_ship)

    if choice > 4:
        for y in range(choice - 4):
            array[cy + y][cx] = 1
    else:
        for x in range(choice):
            array[cy][cx + x] = 1


def remove_rect(grid_y, grid_x, square_size, surface):
    new_ship = pygame.Rect(grid_x, grid_y, square_size, square_size)
    pygame.draw.rect(surface, src.constants.BACKGROUND, new_ship)


def remove_ship(array, cx, cy, square_size, surface):
    direction = 0
    try:
        if array[cy - 1][cx] == 1: 
            direction = 1
    except IndexError:
        pass

    try:
        if array[cy + 1][cx] == 1: 
            direction = 1
    except IndexError:
        pass

    try:
        if array[cy][cx + 1] == 1:
            direction = 2
    except IndexError:
        pass

    try:
        if array[cy][cx - 1] == 1:
            direction = 2
    except IndexError:
        pass


    if direction == 0:
        remove_rect(cy*square_size, cx*square_size, square_size, surface)
        array[cy][cx] = 0
        return 1

    square_counter = 0
    if direction == 1:
        y = 0
        while True:
            try:
                if array[cy - y][cx] == 1:
                    remove_rect((cy - y) * square_size, cx * square_size, square_size, surface)
                    array[cy - y][cx] = 0
                    square_counter += 1
                else:
                    break
            except IndexError:
                break
            y += 1

        y = 1
        while True:
            try:
                if array[cy + y][cx] == 1:
                    remove_rect((cy + y) * square_size, cx * square_size, square_size, surface)
                    array[cy + y][cx] = 0
                    square_counter += 1
                else:
                    break
            except IndexError:
                break
            y += 1

    if direction == 2:
        x = 0
        while True:
            try:
                if array[cy][cx + x] == 1:
                    remove_rect(cy * square_size, (cx + x) * square_size, square_size, surface)
                    array[cy][cx + x] = 0
                    square_counter += 1
                else:
                    break
            except IndexError:
                break
            x += 1

        x = 1
        while True:
            try:
                if array[cy][cx - x] == 1:
                    remove_rect(cy * square_size, (cx - x) * square_size, square_size, surface)
                    array[cy][cx - x] = 0
                    square_counter += 1
                else:
                    break
            except IndexError:
                break
            x += 1
        return square_counter

def main_board_creation(screen, array=np.zeros((10, 10), dtype=int)):
    screen.fill(src.constants.BACKGROUND)
    board = Board(src.constants.BOARD_SIZE, src.constants.BOARD_POS)
    texts = create_text(board)
    selection_buttons = create_ship_buttons(texts)
    run = True
    choice = 0
    texts_dict = {1: 3, 2: 2, 3: 1, 4: 0, 5: 3, 6: 2, 7: 1, 8: 0}
    while run:
        draw_menu(screen, texts, board, selection_buttons)
        x, y = pygame.mouse.get_pos()
        cx, cy, grid_x, grid_y = update(board.board_pos, board.board_size, board.square_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (cy >= 0 and cy <= 9) and (cx >= 0 and cx <= 9) and choice != 0:
                    if check_good_ship_placement(choice, cx, cy, array) and check_length(choice, array, cx, cy):
                        if texts[texts_dict[choice]].value != 0:
                            draw_ship(choice, cx, cy, array, board.surface, board.square_size, grid_x, grid_y)
                            text_rect = pygame.Rect(texts[texts_dict[choice]].x, texts[texts_dict[choice]].y, 50, 50)
                            pygame.draw.rect(screen, src.constants.BACKGROUND, text_rect)
                            texts[texts_dict[choice]].update(texts[texts_dict[choice]].value - 1)
                for button in selection_buttons:
                    collide = button.rect.collidepoint((x, y))
                    if collide:
                        for other_button in selection_buttons:
                            other_button.is_clicked = False
                            other_button.update()
                        button.is_clicked = True
                        button.update()
                        choice = button.ship_type
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if (cy >= 0 and cy <= 9) and (cx >= 0 and cx <= 9):
                    if array[cy][cx] != 0:
                        print(cx, cy)
                        print(grid_x, grid_y)
                        ship_type = remove_ship(array, cx, cy, board.square_size, board.surface)
                        text_rect = pygame.Rect(texts[texts_dict[ship_type]].x, texts[texts_dict[ship_type]].y, 50, 50)
                        pygame.draw.rect(screen, src.constants.BACKGROUND, text_rect)
                        texts[texts_dict[ship_type]].update(texts[texts_dict[ship_type]].value + 1)
        pygame.display.flip()