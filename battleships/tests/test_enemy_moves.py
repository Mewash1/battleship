import random
from battleships.src.enemy_moves import (
    check_if_empty_point,
    check_if_point_can_be_added,
    check_if_point_can_be_shot,
    gen_enemy_moves,
    while_condition,
    go_up,
    go_down,
    go_right,
    go_left,
    remove_duplicates
)
import numpy as np


def test_check_if_empty_point():
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
    assert check_if_empty_point(array, 0, 0) is False
    assert check_if_empty_point(array, 0, 1) is True
    assert check_if_empty_point(array, -1, 0) is False


def test_check_if_point_can_be_added():
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
    assert check_if_point_can_be_added(array, 0, 0) is True
    assert check_if_point_can_be_added(array, 0, 1) is False
    assert check_if_point_can_be_added(array, -1, 0) is False


def test_check_if_point_can_be_shot():
    array = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    assert check_if_point_can_be_shot(array, 0, 0) is True
    assert check_if_point_can_be_shot(array, 0, 1) is True
    assert check_if_point_can_be_shot(array, 0, 2) is False
    assert check_if_point_can_be_shot(array, 0, 3) is True
    assert check_if_point_can_be_shot(array, -1, 0) is False


def test_while_condition():
    array = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    assert while_condition(array, 0, 0) is False
    assert while_condition(array, 0, 1) is True
    assert while_condition(array, 0, 2) is True
    assert while_condition(array, 0, 3) is True
    assert while_condition(array, -1, 0) is True


def test_go_in_four_directions():
    array = np.array(
        [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    up = []
    down = []
    left = []
    right = []
    go_up(array, 4, 2, up)
    go_down(array, 4, 2, down)
    go_left(array, 4, 2, left)
    go_right(array, 4, 2, right)
    assert up == [(4, 1), (4, 0)]
    assert down == [(4, 2), (4, 3), (4, 4)]
    assert left == [(3, 2), (2, 2)]
    assert right == [(4, 2), (5, 2), (6, 2)]


def test_remove_duplicates():
    array = [1, 1, 2, 3, 4, 3, 6, 7, 3, 1, 2]
    new_array = remove_duplicates(array)
    assert new_array == [1, 2, 3, 4, 6, 7]


def test_gen_enemy_moves_vertical(monkeypatch):

    def mock_choice(a):
        return 2

    def mock_randint(a, b):
        return 0
    monkeypatch.setattr(random, 'choice', mock_choice)
    monkeypatch.setattr(random, 'randint', mock_randint)
    array = np.array(
        [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    coords_list = [
                    [(4, 1), (4, 2), (4, 3)],
                    [(4, 2), (4, 0), (4, 3)],
                    [(4, 3), (4, 1), (4, 0)],
                    [(4, 2), (4, 1), (4, 0)]
                ]
    for y in range(0, 4):
        if y == 3:
            def mock_choice(a):
                return 0
            monkeypatch.setattr(random, 'choice', mock_choice)
        coords = gen_enemy_moves(array, 4, y)
        assert coords == coords_list[y]


def test_gen_enemy_moves_horizontal(monkeypatch):

    def mock_choice(a):
        return 1

    def mock_randint(a, b):
        return 0
    monkeypatch.setattr(random, 'choice', mock_choice)
    monkeypatch.setattr(random, 'randint', mock_randint)
    array = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    coords_list = [
                    [(5, 4), (6, 4), (7, 4), (8, 4)],
                    [(6, 4), (7, 4), (8, 4), (4, 4)],
                    [(7, 4), (8, 4), (5, 4), (4, 4)],
                    [(6, 4), (8, 4), (5, 4), (4, 4)]
                ]
    for x in range(4, 8):
        if x == 7:
            def mock_choice(a):
                return 3
            monkeypatch.setattr(random, 'choice', mock_choice)
        coords = gen_enemy_moves(array, x, 4)
        assert coords == coords_list[x - 4]
