import random


def check_if_point_can_be_shot(player_array, ex, ey):
    if ex >= 0 and ex <= 9 and ey >= 0 and ey <= 9 and player_array[ey][ex] != 3:
        return True
    else:
        return False


def check_if_point_can_be_added(player_array, ex, ey):
    if ex >= 0 and ex <= 9 and ey >= 0 and ey <= 9 and player_array[ey][ex] == 1:
        return True
    else:
        return False


def check_if_empty_point(player_array, ex, ey):
    if ex >= 0 and ex <= 9 and ey >= 0 and ey <= 9 and player_array[ey][ex] == 0:
        return True
    else:
        return False


def while_condition(player_array, ex, ey):
    '''
    Checks the conditon for the first while loop.
    '''
    if ex < 0 or ex > 9 or ey < 0 or ey > 9:
        return True
    if player_array[ey][ex] != 1:
        return True
    else:
        return False


def go_up(player_array, ex, ey, coords):
    '''
    Checks coordinates going up.
    '''
    y = 0
    while check_if_point_can_be_added(player_array, ex, ey + y):
        coords.append((ex, ey + y))
        y += 1
    return y


def go_down(player_array, ex, ey, coords):
    '''
    Checks coordinates going down.
    '''
    y = -1
    while check_if_point_can_be_added(player_array, ex, ey + y):
        coords.append((ex, ey + y))
        y -= 1
    return y


def go_right(player_array, ex, ey, coords):
    '''
    Checks coordinates going right.
    '''
    x = 0
    while check_if_point_can_be_added(player_array, ex + x, ey):
        coords.append((ex + x, ey))
        x += 1
    return x


def go_left(player_array, ex, ey, coords):
    '''
    Checks coordinates going left.
    '''
    x = -1
    while check_if_point_can_be_added(player_array, ex + x, ey):
        coords.append((ex + x, ey))
        x -= 1
    return x


def remove_duplicates(array):
    '''
    Removes duplicate entries from the list.
    '''
    new_array = []
    new_set = set()
    for element in array:
        if element not in new_set:
            new_set.add(element)
            new_array.append(element)
    return new_array


def gen_enemy_moves(player_array, ex, ey):
    '''
    By rolling a virtual dice, the game decides which moves are going to be made.\n
    In the first step, computer looks around the given point until it hits another ship cell.\n
    Then, it moves horizontally or vertically to find the rest of the ship.\n
    The game has a 50% chance to move in one direction and 50% chance to move in the opposite direction.\n
    All of the moves are recorded in a list. In the last step, duplicates and the original point are removed from the list.
    '''
    coords = []
    possible_choices = [0, 1, 2, 3]
    original_x = ex
    original_y = ey
    condition = True
    while condition:
        ex = original_x
        ey = original_y
        if len(possible_choices) == 0:
            return []
        choice = random.choice(possible_choices)
        if choice == 0:
            ey -= 1
        elif choice == 1:
            ex += 1
        elif choice == 2:
            ey += 1
        elif choice == 3:
            ex -= 1
        possible_choices.remove(choice)
        if check_if_point_can_be_shot(player_array, ex, ey):
            coords.append((ex, ey))
        condition = while_condition(player_array, ex, ey)

    if len(coords) == 0:
        return coords

    if original_y == ey:
        direction = 1
    elif original_x == ex:
        direction = 2
    ex = coords[-1][0]
    ey = coords[-1][1]
    if direction == 2:
        if random.randint(0, 1) == 0:
            y = go_up(player_array, ex, ey, coords)
            if check_if_empty_point(player_array, ex, ey + y):
                coords.append((ex, ey + y))
            go_down(player_array, ex, ey, coords)
        else:
            y = go_down(player_array, ex, ey, coords)
            if check_if_empty_point(player_array, ex, ey + y):
                coords.append((ex, ey + y))
            go_up(player_array, ex, ey, coords)
    elif direction == 1:
        if random.randint(0, 1) == 0:
            x = go_right(player_array, ex, ey, coords)
            if check_if_empty_point(player_array, ex + x, ey):
                coords.append((ex + x, ey))
            go_left(player_array, ex, ey, coords)
        else:
            x = go_left(player_array, ex, ey, coords)
            if check_if_empty_point(player_array, ex + x, ey):
                coords.append((ex + x, ey))
            go_right(player_array, ex, ey, coords)

    new_coords = remove_duplicates(coords)
    new_coords.remove((original_x, original_y))
    return new_coords
