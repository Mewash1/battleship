import random
from .constants import (
    BACKGROUND,
    BLACK,
    BOARD_SIZE,
    ENEMY_BOARD_POS,
    FONT,
    PLAYER_BOARD_POS,
    BLUE,
    RED,
    WIDTH,
)
from .classes.Board import Board
from .draw_objects import draw_ship
from .array_methods import generate_ship_array, kombajn, update
import pygame
import sys
import numpy as np
from .enemy_moves import gen_enemy_moves


def recreate_board(player_array, surface, square_size, color=(255, 255, 255)):
    '''
    Draws all ships on player's board according to player's array.
    '''
    for y in range(0, 10):
        for x in range(0, 10):
            if player_array[y][x] == 1:
                draw_ship(
                    1, surface, square_size, x * square_size, y * square_size, color
                )
            if player_array[y][x] == 3:
                draw_ship(
                    1, surface, square_size, x * square_size, y * square_size, BLUE
                )


def draw_two_boards(player_board, enemy_board, player_array, screen):
    '''
    Draw both player's and enemy's board on screen.
    '''
    recreate_board(player_array, player_board.surface, player_board.square_size)
    player_board.draw_board()
    screen.blit(player_board.surface, player_board.board_pos)
    enemy_board.draw_board()
    screen.blit(enemy_board.surface, enemy_board.board_pos)


def choose_a_random_point(player_array):
    '''
    Chooses a random point that fits on the board and was not shot before.
    '''
    while True:
        ex = random.randint(0, 9)
        ey = random.randint(0, 9)
        if player_array[ey][ex] != 2 and player_array[ey][ex] != 3:
            return ex, ey


def enemy_turn(player_array, player_board, coords):
    '''
    Executes the enemy turn.\n
    The computer has two states. In the first state, it shoots randomly until it hits a ship.\n
    Then a list with coordinates is generated that the computer executes. When the instructions end, it returns to the first state.
    '''
    if coords is None:
        coords = []
    while len(coords) != 0:
        ex, ey = coords[0][0], coords[0][1]
        if player_array[ey][ex] == 3:
            coords = coords[1:]
        else:
            break
    if len(coords) == 0:
        ex, ey = choose_a_random_point(player_array)

    if player_array[ey][ex] == 0:
        draw_ship(
            1,
            player_board.surface,
            player_board.square_size,
            ex * player_board.square_size,
            ey * player_board.square_size,
            color=BLUE,
        )
        player_array[ey][ex] = 3
    elif player_array[ey][ex] == 1:
        draw_ship(
            1,
            player_board.surface,
            player_board.square_size,
            ex * player_board.square_size,
            ey * player_board.square_size,
            color=RED,
        )
        if coords is not None:
            if len(coords) == 0:
                coords = gen_enemy_moves(player_array, ex, ey)
            else:
                coords = coords[1:]
        player_array[ey][ex] = 2
        if not kombajn(
            player_array,
            ex,
            ey,
            player_board.square_size,
            player_board.surface,
            False,
            False,
        )[1]:
            kombajn(
                player_array,
                ex,
                ey,
                player_board.square_size,
                player_board.surface,
                True,
                False,
            )
    return coords



def player_turn(cx, cy, player_array, enemy_array, player_board, coords, enemy_board, grid_x, grid_y):
    '''
    Executes the player turn, and then immediately after the enemy's turn.\n
    If the player hits a ship, the game checks if this was the last cell of a given ship.\n
    If yes, then the area around the ship is colored blue.
    '''
    if (cy >= 0 and cy <= 9) and (cx >= 0 and cx <= 9):
        if enemy_array[cy][cx] == 0:
            draw_ship(
                1,
                enemy_board.surface,
                enemy_board.square_size,
                grid_x,
                grid_y,
                color=BLUE,
            )
            enemy_array[cy][cx] = 3
            coords = enemy_turn(player_array, player_board, coords)
        elif enemy_array[cy][cx] == 1:
            draw_ship(
                1,
                enemy_board.surface,
                enemy_board.square_size,
                grid_x,
                grid_y,
                color=RED,
            )
            enemy_array[cy][cx] = 2
            if not kombajn(
                enemy_array,
                cx,
                cy,
                enemy_board.square_size,
                enemy_board.surface,
                False,
                False,
            )[1]:
                kombajn(
                    enemy_array,
                    cx,
                    cy,
                    enemy_board.square_size,
                    enemy_board.surface,
                    True,
                    False,
                )
            coords = enemy_turn(player_array, player_board, coords)
        return coords


def check_win_condition_for_array(array):
    '''
    Checks if there are any unsunken ships left on the given board.
    '''
    for element in np.nditer(array):
        if element == 1:
            return False
    return True


def show_postgame_message(screen, message, x, y):
    '''
    Shows a given message on screen.
    '''
    win_text = FONT.render(message, True, BLACK)
    win_rect = win_text.get_rect()
    win_rect.x = x
    win_rect.y = y
    screen.blit(win_text, win_rect)


def check_win_condition(screen, enemy_array, player_array):
    '''
    Checks if the player or the computer has won the game.\n
    If true, it shows the appropiate message on screen and starts a new loop that can only be broken by exiting the game.
    '''
    player_win_condition = check_win_condition_for_array(enemy_array)
    enemy_win_condition = check_win_condition_for_array(player_array)
    if player_win_condition or enemy_win_condition:
        if enemy_win_condition and player_win_condition:
            show_postgame_message(
                screen,
                "DRAW! Nobody has won!",
                WIDTH / 2 - 200,
                500,
            )
        elif enemy_win_condition:
            show_postgame_message(
                screen,
                "DEFEAT! You have lost the game...",
                WIDTH / 2 - 200,
                500,
            )
        elif player_win_condition:
            show_postgame_message(
                screen,
                "VICTORY! You have won the game",
                WIDTH / 2 - 200,
                500,
            )
        show_postgame_message(screen, "Press ENTER to exit", WIDTH / 2 - 200, 550)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        sys.exit()


def main_third_screen(screen, player_array):
    screen.fill(BACKGROUND)
    player_board = Board(BOARD_SIZE, PLAYER_BOARD_POS)
    enemy_board = Board(BOARD_SIZE, ENEMY_BOARD_POS)
    enemy_array = generate_ship_array()
    coords = []
    run = True

    while run:
        draw_two_boards(player_board, enemy_board, player_array, enemy_array, screen)
        check_win_condition(screen, enemy_array, player_array)
        cx, cy, grid_x, grid_y = update(
            enemy_board.board_pos, enemy_board.board_size, enemy_board.square_size
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coords = player_turn(cx, cy, player_array, enemy_array, player_board, coords, enemy_board, grid_x, grid_y)
        pygame.display.flip()
