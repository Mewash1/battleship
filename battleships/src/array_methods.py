from .draw_objects import remove_rect


def get_direction(array, cx, cy):
    '''
    Checks cells in four directions to check if 
    '''
    direction = 0
    try:
        if array[cy - 1][cx] == 1: 
            direction = 1
    except IndexError:
        pass

    try:
        if array[cy + 1][cx] == 1: 
            direction = 1
    except IndexError:
        pass

    try:
        if array[cy][cx + 1] == 1:
            direction = 2
    except IndexError:
        pass

    try:
        if array[cy][cx - 1] == 1:
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
    if direction == 0:
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