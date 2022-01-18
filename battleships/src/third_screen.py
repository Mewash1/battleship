from random import randint, random
from .constants import BACKGROUND, BOARD_SIZE, ENEMY_BOARD_POS, PLAYER_BOARD_POS, BLUE, RED
from .classes.Board import Board
from .draw_objects import draw_ship
from .array_methods import check_if_ship, generate_ship_array, kombajn, turn_area_around_ship_blue, update
import pygame
import sys
import numpy as np


def recreate_board(player_array, surface, square_size, color=(255, 255, 255)):
    for y in range(0, 10):
        for x in range(0, 10):
            if player_array[y][x] == 1:
                draw_ship(1, surface, square_size, x * square_size, y * square_size, color)
            if player_array[y][x] == 3:
                draw_ship(1, surface, square_size, x * square_size, y * square_size, BLUE)


def draw_two_boards(player_board, enemy_board, player_array, enemy_array, screen):
    recreate_board(player_array, player_board.surface, player_board.square_size)
    # for debugging only!
    recreate_board(enemy_array, enemy_board.surface, enemy_board.square_size)
    player_board.draw_board()
    screen.blit(player_board.surface, player_board.board_pos)
    enemy_board.draw_board()
    screen.blit(enemy_board.surface, enemy_board.board_pos)


def choose_a_random_point(player_array):
    while True:
        ex = randint(0, 9)
        ey = randint(0, 9)
        if player_array[ey][ex] != 2 and player_array[ey][ex] != 3:
            return ex, ey


def enemy_turn(player_array, player_board, enemy_set=None, enemy_array=None):
    ex, ey = choose_a_random_point(player_array)
    if player_array[ey][ex] == 0:
        draw_ship(1, player_board.surface, player_board.square_size, ex * player_board.square_size, ey * player_board.square_size, color=BLUE)
        player_array[ey][ex] = 3
    elif player_array[ey][ex] == 1:
        draw_ship(1, player_board.surface, player_board.square_size, ex * player_board.square_size, ey * player_board.square_size, color=RED)
        player_array[ey][ex] = 2
        if not kombajn(player_array, ex, ey, player_board.square_size, player_board.surface, False, False)[1]:
            kombajn(player_array, ex, ey, player_board.square_size, player_board.surface, True, False)



def main_third_screen(screen, player_array):
    print(player_array)
    screen.fill(BACKGROUND)
    player_board = Board(BOARD_SIZE, PLAYER_BOARD_POS)
    enemy_board = Board(BOARD_SIZE, ENEMY_BOARD_POS)
    enemy_array = generate_ship_array()
    enemy_set = set()
    '''
    enemy_array = np.zeros((10, 10), dtype=int)
    enemy_array[0][0], enemy_array[0][1], enemy_array[0][2] = 2, 2, 2
    enemy_array[0][3] = 1
    '''
    run = True

    while run:
        draw_two_boards(player_board, enemy_board, player_array, enemy_array, screen)
        x, y = pygame.mouse.get_pos()
        cx, cy, grid_x, grid_y = update(enemy_board.board_pos, enemy_board.board_size, enemy_board.square_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (cy >= 0 and cy <= 9) and (cx >= 0 and cx <= 9):
                    if enemy_array[cy][cx] == 0:
                        draw_ship(1, enemy_board.surface, enemy_board.square_size, grid_x, grid_y, color=BLUE)
                        enemy_array[cy][cx] = 3
                        enemy_turn(player_array, player_board, enemy_set, enemy_array)
                    elif enemy_array[cy][cx] == 1:
                        draw_ship(1, enemy_board.surface, enemy_board.square_size, grid_x, grid_y, color=RED)
                        enemy_array[cy][cx] = 2
                        if not check_if_ship(enemy_array, cx, cy):
                            kombajn(enemy_array, cx, cy, enemy_board.square_size, enemy_board.surface, True, False)
                        enemy_turn(player_array, player_board)

                        
        pygame.display.flip()