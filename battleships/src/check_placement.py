from ast import Index
import numpy


def check_for_ships_around_point(cx, cy, array):
    print(cx, cy)
    try:
        if array[cy][cx] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy - 1][cx] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy + 1][cx] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy][cx - 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy][cx + 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy - 1][cx - 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy + 1][cx + 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy - 1][cx + 1] != 0:
            return False
    except IndexError:
        pass
    try:
        if array[cy + 1][cx - 1] != 0:
            return False
    except IndexError:
        pass
    return True


def check_good_ship_placement(choice, cx, cy, array):
    if choice in {1, 2, 3, 4}:
        for x in range(choice):
            if not check_for_ships_around_point(cx + x, cy, array):
                return False
    elif choice in {5, 6, 7, 8}:
        for y in range(choice - 4):
            if not check_for_ships_around_point(cx, cy + y, array):
                return False
    return True


def check_length(choice, array, cx, cy):
    if choice == 1 or choice == 5:
        return True
    else:
        if choice in {2, 3, 4}:
            for x in range(choice):
                try:
                    if array[cy][cx + x] != 0:
                        return False
                except IndexError:
                    return False
        elif choice in {6, 7, 8}:
            for y in range(choice - 4):
                try:
                    if array[cy + y][cx] != 0:
                        return False
                except IndexError:
                    return False
        return True
