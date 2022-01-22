import pygame
from .third_screen import main_third_screen
from .constants import BACKGROUND, BOARD_POS, BOARD_SIZE
import numpy as np
import sys
from .check_placement import check_good_ship_placement, check_length
from .classes.Board import Board
from .draw_objects import draw_menu, draw_ship
from .array_methods import kombajn, update_array
from .create_objects import create_submit_button, create_rotate_button, create_ship_buttons, create_text
from .array_methods import update


def check_draw_submit(texts):
    '''
    Checks if the player has put down all of their ships.
    '''
    for text in texts:
        if text.value != 0:
            return False
    return True


def use_rotation(rotate_button, choice):
    '''
    Operates rotation button. Based on its state, the function changes the choice value.
    '''
    if rotate_button.is_clicked:
        rotate_button.is_clicked = False
        rotate_button.update()
        if choice != 0:
            choice = choice - 4
    else:
        rotate_button.is_clicked = True
        rotate_button.update()
        if choice != 0:
            choice = choice + 4
    return rotate_button, choice


def selection_button_click(selection_buttons, rotate_button, x, y, choice):
    '''
    Check if a selection button was pressed and then changes the choice value accordingly.
    '''
    for button in selection_buttons:
        collide = button.rect.collidepoint((x, y))
        if collide:
            for other_button in selection_buttons:
                other_button.is_clicked = False
                other_button.update()
                button.is_clicked = True
                button.update()
                if rotate_button.is_clicked:
                    choice = button.ship_type + 4
                else:
                    choice = button.ship_type
    return selection_buttons, rotate_button, choice


def put_ship_down(choice, cx, cy, array, board, grid_x, grid_y, texts, texts_dict, screen):
    '''
    Draws the chosen ship, updates the text beside the button and updates the array.
    '''
    draw_ship(choice, board.surface, board.square_size, grid_x, grid_y)
    update_array(choice, cx, cy, array)
    text_rect = pygame.Rect(texts[texts_dict[choice]].x, texts[texts_dict[choice]].y, 50, 50)
    pygame.draw.rect(screen, BACKGROUND, text_rect)
    texts[texts_dict[choice]].update(texts[texts_dict[choice]].value - 1)
                

def right_click(cx, cy, array, board, texts, texts_dict, screen):
    '''
    Removes the clicked ship, updates the text beside the button and updates the array.
    '''
    ship_type = kombajn(array, cx, cy, board.square_size, board.surface, False, True)[0]
    text_rect = pygame.Rect(texts[texts_dict[ship_type]].x, texts[texts_dict[ship_type]].y, 50, 50)
    pygame.draw.rect(screen, BACKGROUND, text_rect)
    texts[texts_dict[ship_type]].update(texts[texts_dict[ship_type]].value + 1)


def main_second_screen(screen, array=np.zeros((10, 10), dtype=int)):
    screen.fill(BACKGROUND)
    board = Board(BOARD_SIZE, BOARD_POS)
    texts = create_text(board)
    selection_buttons = create_ship_buttons(texts)
    rotate_button = create_rotate_button(board)
    submit_button = create_submit_button(board)
    run = True
    choice = 0
    texts_dict = {1: 3, 2: 2, 3: 1, 4: 0, 5: 3, 6: 2, 7: 1, 8: 0}
    while run:
        draw_menu(screen, texts, board, selection_buttons, rotate_button)
        x, y = pygame.mouse.get_pos()
        cx, cy, grid_x, grid_y = update(board.board_pos, board.board_size, board.square_size)
        if check_draw_submit(texts):
            submit_button.draw(screen)
            submit_button.is_clickable = True
        else:
            bckg_rect = pygame.Rect(submit_button.x, submit_button.y, submit_button.rect.width, submit_button.rect.height)
            pygame.draw.rect(screen, BACKGROUND, bckg_rect)
            submit_button.is_clickable = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                if rotate_button.rect.collidepoint((x, y)):
                    rotate_button, choice = use_rotation(rotate_button, choice)

                if submit_button.rect.collidepoint((x, y)) and submit_button.is_clickable:
                    main_third_screen(screen, array)

                selection_buttons, rotate_button, choice = selection_button_click(selection_buttons, rotate_button, x, y, choice)

                if (cy >= 0 and cy <= 9) and (cx >= 0 and cx <= 9) and choice != 0:
                    if check_good_ship_placement(choice, cx, cy, array) and check_length(choice, array, cx, cy):
                        if texts[texts_dict[choice]].value != 0:
                            put_ship_down(choice, cx, cy, array, board, grid_x, grid_y, texts, texts_dict, screen)
                
            # right click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if (cy >= 0 and cy <= 9) and (cx >= 0 and cx <= 9):
                    if array[cy][cx] != 0:
                        right_click(cx, cy, array, board, texts, texts_dict, screen)

        pygame.display.flip()
