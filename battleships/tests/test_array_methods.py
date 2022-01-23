from battleships.src.array_methods import (
    analyze_whole_ship,
    get_direction,
    analyze_point,
    update_array,
    update,
    check_win_condition_for_array,
    choose_a_random_point)
import numpy as np
import pygame
import random
from battleships.src.constants import SIZE


def test_get_direction_horziontal():
    array = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    cy = 4
    cx = 3
    for x in range(0, 4):
        assert get_direction(array, cx + x, cy) == 2


def test_get_direction_vertical():
    array = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    cy = 1
    cx = 3
    for y in range(0, 4):
        assert get_direction(array, cx, cy + y) == 1


def test_get_direction_single_square():
    array = np.array(
        [
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    cy = 0
    cx = 0
    assert get_direction(array, cx, cy) == 0


def test_analyze_point_color():
    array = np.array(
        [
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    cy = 0
    cx = 0
    screen = pygame.Surface(SIZE)
    x = 0
    y = 0
    square_counter, check = analyze_point(array, cx, cy, 10, screen, True, False, 0, x, y, False)
    assert array[0][0] == 2
    assert array[0][1] == 3
    assert array[1][0] == 3
    assert array[1][1] == 3
    assert array[9][0] == 0
    assert array[9][1] == 0
    assert check is False
    assert square_counter == 0


def test_analyze_point_remove():
    array = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    cy = 0
    cx = 0
    screen = pygame.Surface(SIZE)
    x = 0
    y = 0
    square_counter, check = analyze_point(array, cx, cy, 10, screen, False, True, 0, x, y, False)
    assert array[0][0] == 0
    assert check is True
    assert square_counter == 1


def test_analyze_whole_ship_color_horizontally():
    screen = pygame.Surface(SIZE)
    cx = 3
    cy = 4
    for _ in range(0, 4):
        array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
        analyze_whole_ship(array, cx, cy, 12, screen, True, False)
        for x in range(2, 8):
            assert array[3][x] == 3
        for x in range(2, 8):
            assert array[5][x] == 3
        assert array[4][2] == 3
        assert array[4][7] == 3
        cx += 1


def test_analyze_whole_ship_remove_horizontally():
    screen = pygame.Surface(SIZE)
    cx = 3
    cy = 4
    for _ in range(0, 4):
        array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
        square_counter, check = analyze_whole_ship(array, cx, cy, 12, screen, False, True)
        assert square_counter == 4
        assert check is True
        assert array[4][3] == 0
        assert array[4][4] == 0
        assert array[4][5] == 0
        assert array[4][6] == 0
        cx += 1


def test_analyze_whole_ship_color_vertically():
    screen = pygame.Surface(SIZE)
    cx = 3
    cy = 4
    for _ in range(0, 4):
        array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
        analyze_whole_ship(array, cx, cy, 12, screen, True, False)
        for y in range(4, 9):
            assert array[y][2] == 3
        for y in range(4, 9):
            assert array[y][4] == 3
        assert array[3][3] == 3
        assert array[8][3] == 3
        cy += 1


def test_analyze_whole_ship_remove_vertically():
    screen = pygame.Surface(SIZE)
    cx = 3
    cy = 4
    for _ in range(0, 4):
        array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
        square_counter, check = analyze_whole_ship(array, cx, cy, 12, screen, False, True)
        assert square_counter == 4
        assert check is True
        assert array[4][3] == 0
        assert array[5][3] == 0
        assert array[6][3] == 0
        assert array[7][3] == 0
        cy += 1


def test_analyze_whole_ship_color_one_square():
    screen = pygame.Surface(SIZE)
    array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
    analyze_whole_ship(array, 3, 4, 12, screen, True, False)
    for y in range(-1, 2):
        for x in range(-1, 2):
            if array[4][3] != 2:
                assert array[4 + y][3 + x] == 3


def test_analyze_whole_ship_remove_one_square():
    screen = pygame.Surface(SIZE)
    array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
    square_counter, check = analyze_whole_ship(array, 3, 4, 12, screen, False, True)
    assert array[4][3] == 0
    assert square_counter == 1
    assert check is False


def test_update_array():
    array = np.zeros((10, 10), dtype=int)
    update_array(4, 0, 0, array)
    update_array(7, 4, 5, array)
    print(array)
    for x in range(0, 4):
        assert array[0][x] == 1
    for y in range(5, 8):
        assert array[y][4] == 1


def test_update(monkeypatch):
    def mock_func():
        return 91, 123
    monkeypatch.setattr(pygame.mouse, 'get_pos', mock_func)
    board_pos = (0, 0)
    board_size = (300, 300)
    cx, cy, grid_x, grid_y = update(board_pos, board_size, 10)
    assert cx == 3
    assert cy == 4
    assert grid_x == 90
    assert grid_y == 120


def test_check_win_condition_for_array():
    array_1 = np.zeros((10, 10))
    assert check_win_condition_for_array(array_1) is True
    array_1[5][6] = 2
    assert check_win_condition_for_array(array_1) is True
    array_1[3][8] = 1
    assert check_win_condition_for_array(array_1) is False


def test_choose_a_random_point(monkeypatch):
    array_1 = np.zeros((10, 10))

    def mock_randint(a, b):
        return 0
    monkeypatch.setattr(random, 'randint', mock_randint)
    ex, ey = choose_a_random_point(array_1)
    assert ex == 0
    assert ey == 0
