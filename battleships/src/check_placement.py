def check_for_ships_around_point(cx, cy, array):
    '''
    Checks if there are any ships around the given point.
    '''
    for y in range(-1, 2):
        for x in range(-1, 2):
            try:
                if array[cy + y][cx + x] != 0 and cy + y >= 0 and cx + x >= 0:
                    return False
            except IndexError:
                pass
    return True


def check_good_ship_placement(choice, cx, cy, array):
    '''
    Checks if there is a ship around the given ships.\n
    The cx, cy coordinates refer to the leftmost or to the upmost part of the ship, depending on direction.
    '''
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
    '''
    Checks if the given ship fits on the board.
    '''
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
