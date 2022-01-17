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


def remove_ship(array, cx, cy, square_size, surface):
    '''
    First, the function checks if the ship is alinged vertically or horizontally. (If neither, it's just a single square.)\n
    Then it check all of the cells in that direction - left and right, or up and down. This continues as long as function either:\n
    - checks a spot out of bounds,\n
    - encounters an empty cell\n
    in which case it stops. Since all of the ships are assumed to be put down in accordance to the rules, this function works well.
    '''
  
    direction = get_direction(array, cx, cy)
    if direction == 0 and array[cy][cx] == 1:
        remove_rect(cy*square_size, cx*square_size, square_size, surface)
        array[cy][cx] = 0
        return 1

    square_counter = 0
    if direction == 1:
        y = 0
        while True:
            try:
                if array[cy - y][cx] == 1 and cy != 0:
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
                if array[cy][cx - x] == 1 and cx != 0:
                    remove_rect(cy * square_size, (cx - x) * square_size, square_size, surface)
                    array[cy][cx - x] = 0
                    square_counter += 1
                else:
                    break
            except IndexError:
                break
            x += 1
    
    return square_counter



def check_if_ship(array, cx, cy):
    check = False
    direction = get_direction(array, cx, cy)
    if direction == 0:
        return False

    if direction == 1:
        y = 1
        while True:
            try:
                if array[cy - y][cx] == 1 and cy - y != 0:
                    return True
                elif array[cy - y][cx] == 2 and cy - y != 0:
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
                    return True
                elif array[cy + y][cx] == 2:
                    y += 1
                    continue
                else:
                    break
            except IndexError:
                break

    if direction == 2:
        x = 1
        while True:
            try:
                if array[cy][cx + x] == 1:
                    return True
                elif array[cy][cx + x] == 2:
                    x += 1
                    continue
                else:
                    break
            except IndexError:
                break

        x = 1
        while True:
            try:
                if array[cy][cx - x] == 1 and cx - x != 0:
                    return True
                elif array[cy][cx - x] == 2 and cx - x != 0:
                    x += 1
                    continue
                else:
                    break
            except IndexError:
                break
    return False


def turn_area_around_ship_blue(array, cx, cy, surface, square_size):
    direction = get_direction(array, cx, cy)
    if direction == 0:
        turn_squares_blue_around_point(cx, cy, array, surface, square_size)

    if direction == 1:
        y = 0
        while True:
            try:
                if array[cy - y][cx] == 2 and cy - y != 0:
                    turn_squares_blue_around_point(cx, cy - y, array, surface, square_size)
                    y += 1
                else:
                    break
            except IndexError:
                break

        y = 1
        while True:
            try:
                if array[cy + y][cx] == 2:
                    turn_squares_blue_around_point(cx, cy + y, array, surface, square_size)
                    y += 1
                else:
                    break
            except IndexError:
                break

    if direction == 2:
        x = 0
        while True:
            try:
                if array[cy][cx + x] == 2:
                    turn_squares_blue_around_point(cx + x, cy, array, surface, square_size)
                    x += 1
                else:
                    break
            except IndexError:
                break

        x = 1
        while True:
            try:
                if array[cy][cx - x] == 2 and cx - x != 0:
                    turn_squares_blue_around_point(cx - x, cy, array, surface, square_size)
                    x += 1
                else:
                    break
            except IndexError:
                break


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