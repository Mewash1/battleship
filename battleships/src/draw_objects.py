import pygame
from .constants import BLUE


def draw_ship(choice, surface, square_size, grid_x, grid_y, color=(255, 255, 255)):
    """
    Draws a given ship of a given color.
    """
    choice_dict = {
        1: (1, 1),
        2: (2, 1),
        3: (3, 1),
        4: (4, 1),
        5: (1, 1),
        6: (1, 2),
        7: (1, 3),
        8: (1, 4),
    }
    height = square_size * choice_dict[choice][0]
    width = square_size * choice_dict[choice][1]
    new_ship = pygame.Rect(grid_x, grid_y, height, width)
    pygame.draw.rect(surface, color, new_ship)


def draw_menu(screen, texts, board, selection_buttons, rotate_button):
    """
    Draws the board, texts and the buttons.
    """
    board.draw_board()
    screen.blit(board.surface, board.board_pos)
    rotate_button.draw(screen)
    for text in texts:
        text.draw(screen)
    for button in selection_buttons:
        button.draw(screen)


def turn_squares_blue_around_point(cx, cy, array, surface, square_size):
    '''
    Turns all squares that are empty into blue ones around the given point.
    '''
    for y in range(-1, 2):
        for x in range(-1, 2):
            try:
                if array[cy + y][cx + x] != 2 and cy + y >= 0 and cx + x >= 0:
                    array[cy + y][cx + x] = 3
                    draw_ship(
                        1,
                        surface,
                        square_size,
                        (cx + x) * square_size,
                        (cy + y) * square_size,
                        BLUE,
                    )
            except IndexError:
                pass
