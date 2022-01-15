import pygame
from .constants import BACKGROUND 


def draw_ship(choice, surface, square_size, grid_x, grid_y):
    '''
    Draws ship on the board.
    '''
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



def remove_rect(grid_y, grid_x, square_size, surface):
    '''
    Removes a single cell of the ship.
    '''
    new_ship = pygame.Rect(grid_x, grid_y, square_size, square_size)
    pygame.draw.rect(surface, BACKGROUND, new_ship)


def draw_menu(screen, texts, board, selection_buttons, rotate_button):
    '''
    Draws the board, texts and the buttons.
    '''
    board.draw_board()
    screen.blit(board.surface, board.board_pos)
    rotate_button.draw(screen)
    for text in texts:
        text.draw(screen)
    for button in selection_buttons:
        button.draw(screen)