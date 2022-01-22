from .constants import BACKGROUND
from .check_placement import (
    check_for_ships_around_point,
    check_good_ship_placement,
    check_length,
)
from .draw_objects import draw_ship, turn_squares_blue_around_point
import random
import numpy as np
import pygame


def get_direction(array, cx, cy):
    """
    Checks cells in four directions to check if
    """
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


def analyze_point(
    array,
    cx,
    cy,
    square_size,
    surface,
    check_if_color,
    check_if_remove,
    square_counter,
    x,
    y,
    check
):
    if array[cy + y][cx + x] == 1:
        if check_if_remove:
            draw_ship(
                1,
                surface,
                square_size,
                (cx + x) * square_size,
                (cy + y) * square_size,
                BACKGROUND,
            )
            array[cy + y][cx + x] = 0
            square_counter += 1
        check = True
    elif array[cy + y][cx + x] == 2:
        if check_if_color:
            turn_squares_blue_around_point(cx + x, cy + y, array, surface, square_size)
    return square_counter, check


def kombajn(
    array, cx, cy, square_size, surface, check_if_color, check_if_remove
):
    check = False
    direction = get_direction(array, cx, cy)
    square_counter = 1
    if check_if_remove:
        draw_ship(
            1, surface, square_size, cx * square_size, cy * square_size, BACKGROUND
        )
        array[cy][cx] = 0
    if check_if_color:
        turn_squares_blue_around_point(cx, cy, array, surface, square_size)
    if direction == 0:
        if check_if_color:
            return None, None
        else:
            return 1, False
    elif direction == 1:
        y = 0
        x = 0
        try:
            while array[cy + y][cx] == 1 or array[cy + y][cx] == 2:
                square_counter, check = analyze_point(
                    array,
                    cx,
                    cy,
                    square_size,
                    surface,
                    check_if_color,
                    check_if_remove,
                    square_counter,
                    x,
                    y,
                    check
                )
                y += 1
        except IndexError:
            pass
        y = -1
        try:
            while array[cy + y][cx] == 1 or array[cy + y][cx] == 2:
                square_counter, check = analyze_point(
                    array,
                    cx,
                    cy,
                    square_size,
                    surface,
                    check_if_color,
                    check_if_remove,
                    square_counter,
                    x,
                    y,
                    check
                )
                y -= 1
        except IndexError:
            pass
    elif direction == 2:
        y = 0
        x = 0
        try:
            while array[cy][cx + x] == 1 or array[cy][cx + x] == 2:
                square_counter, check = analyze_point(
                    array,
                    cx,
                    cy,
                    square_size,
                    surface,
                    check_if_color,
                    check_if_remove,
                    square_counter,
                    x,
                    y,
                    check
                )
                x += 1
        except IndexError:
            pass
        x = -1
        try:
            while array[cy][cx + x] == 1 or array[cy][cx + x] == 2:
                square_counter, check = analyze_point(
                    array,
                    cx,
                    cy,
                    square_size,
                    surface,
                    check_if_color,
                    check_if_remove,
                    square_counter,
                    x,
                    y,
                    check
                )
                x -= 1
        except IndexError:
            pass
    print(check)
    return square_counter, check


def update_array(choice, cx, cy, array):
    """
    Updates the array after drawing the ship on the board.\n
    The two must be in sync with each other, since the array will be later used for redrawing the board\n
    and is actively used to check for ship collisions.
    """
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
            if check_good_ship_placement(choice + v, x, y, array) and check_length(
                choice + v, array, x, y
            ):
                update_array(choice + v, x, y, array)
                num_of_ships -= 1
        choice -= 1
        num_of_ships = 5 - choice

    return array


def update(board_pos, board_size, square_size):
    """
    Returns the coordinates of mouse in terms of board. Each cell has a specific coordinate (eg. top-right corner is (0, 9))\n
    By getting the coords like this it's then very easy to search the board array for necessary values.\n
    The function also returns the coords without dividing them by the size of the cell. It's useful for drawing.
    """
    x, y = pygame.mouse.get_pos()
    x, y = x - board_pos[0], y - board_pos[1]
    grid_x = x // square_size
    grid_y = y // square_size
    cx, cy = grid_x * square_size, grid_y * square_size
    return int(cx / (board_size[0] // 10)), int(cy / (board_size[0] // 10)), cx, cy
