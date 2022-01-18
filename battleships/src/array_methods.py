from .constants import BACKGROUND, RED
from .check_placement import check_for_ships_around_point, check_good_ship_placement, check_length
from .draw_objects import draw_ship, remove_rect, turn_squares_blue_around_point
import random
import numpy as np
import pygame


def get_direction(array, cx, cy):
    '''
    Checks cells in four directions to check if 
    '''
    direction = 0
    try:
        if array[cy - 1][cx] == 1 or array[cy - 1][cx] == 2:
            direction = 1
    except IndexError:
        pass

    try:
        if array[cy + 1][cx] == 1 or array[cy + 1][cx] == 2:
            direction = 1
    except IndexError:
        pass

    try:
        if array[cy][cx + 1] == 1 or array[cy][cx + 1] == 2:
            direction = 2
    except IndexError:
        pass

    try:
        if array[cy][cx - 1] == 1 or array[cy][cx - 1] == 2:
            direction = 2
    except IndexError:
        pass

    return direction


def kombajn(array, cx, cy, square_size, surface, check_or_color, check_if_remove):
    check = False
    coords = []
    direction = get_direction(array, cx, cy)
    if direction == 0:
        if array[cy][cx] == 1:
            remove_rect(cy*square_size, cx*square_size, square_size, surface)
            array[cy][cx] = 0
            return 1, None
        elif array[cy][cx] == 2:
            if check_or_color:
                turn_squares_blue_around_point(cx, cy, array, surface, square_size)
                return None, None
            else:
                return None, False, None
            

    square_counter = 1
    if check_if_remove:
        remove_rect(cy*square_size, cx*square_size, square_size, surface)
        array[cy][cx] = 0
    if check_or_color:
        turn_squares_blue_around_point(cx, cy, array, surface, square_size)
    if direction == 1:
        y = 1
        while True:
            try:
                if array[cy - y][cx] == 1 and cy != 0:
                    if check_if_remove:
                        remove_rect((cy - y) * square_size, cx * square_size, square_size, surface)
                        array[cy - y][cx] = 0
                        square_counter += 1
                    coords.append((cy - y, cx))
                    y += 1
                    check = True
                elif array[cy - y][cx] == 2 and cy - y != 0:
                    if check_or_color:
                        turn_squares_blue_around_point(cx, cy - y, array, surface, square_size)
                    y += 1
                    continue
                else:
                    break
            except IndexError:
                break

        y = 1
        while True:
            try:
                if array[cy + y][cx] == 1:
                    if check_if_remove:
                        remove_rect((cy + y) * square_size, cx * square_size, square_size, surface)
                        array[cy + y][cx] = 0
                        square_counter += 1
                    coords.append((cy + y, cx))
                    y += 1
                    check = True
                elif array[cy + y][cx] == 2:
                    if check_or_color:
                        turn_squares_blue_around_point(cx, cy + y, array, surface, square_size)
                    y += 1
                else:
                    break
            except IndexError:
                break
            

    if direction == 2:
        x = 1
        while True:
            try:
                if array[cy][cx + x] == 1:
                    if check_if_remove:
                        remove_rect(cy * square_size, (cx + x) * square_size, square_size, surface)
                        array[cy][cx + x] = 0
                        square_counter += 1
                    coords.append((cy, cx + x))
                    x += 1
                    check = True
                elif array[cy][cx + x] == 2:
                    if check_or_color:
                        turn_squares_blue_around_point(cx + x, cy, array, surface, square_size)
                    x += 1
                else:
                    break
            except IndexError:
                break
            

        x = 1
        while True:
            try:
                if array[cy][cx - x] == 1:
                    if check_if_remove:
                        remove_rect(cy * square_size, (cx - x) * square_size, square_size, surface)
                        array[cy][cx - x] = 0
                        square_counter += 1
                    coords.append((cy, cx - x))
                    x += 1
                    check = True
                elif array[cy][cx - x] == 2:
                    if check_or_color:
                        turn_squares_blue_around_point(cx - x, cy, array, surface, square_size)
                    x += 1
                else:
                    break
            except IndexError:
                break
            
    
    return square_counter, check, coords


def update_array(choice, cx, cy, array):
    '''
    Updates the array after drawing the ship on the board.\n
    The two must be in sync with each other, since the array will be later used for redrawing the board\n
    and is actively used to check for ship collisions.
    '''
    if choice > 4:
        for y in range(choice - 4):
            array[cy + y][cx] = 1
    else:
        for x in range(choice):
            array[cy][cx + x] = 1


def generate_ship_array():
    choice = 4
    num_of_ships = 1
    array = np.zeros((10, 10), dtype=int)
    while choice != 0:
        while num_of_ships != 0:
            v = random.choice((0, 4))
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if check_good_ship_placement(choice + v, x, y, array) and check_length(choice + v, array, x, y):
                update_array(choice + v, x, y, array)
                num_of_ships -= 1
        choice -= 1
        num_of_ships = 5 - choice

    return array


def update(board_pos, board_size, square_size):
    '''
    Returns the coordinates of mouse in terms of board. Each cell has a specific coordinate (eg. top-right corner is (0, 9))\n
    By getting the coords like this it's then very easy to search the board array for necessary values.\n
    The function also returns the coords without dividing them by the size of the cell. It's useful for drawing.
    '''
    x, y = pygame.mouse.get_pos()
    x, y = x - board_pos[0], y - board_pos[1]
    grid_x = x // square_size
    grid_y = y // square_size
    cx, cy = grid_x * square_size, grid_y * square_size
    return int(cx/(board_size[0]//10)), int(cy/(board_size[0]//10)), cx, cy