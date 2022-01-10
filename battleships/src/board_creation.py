import pygame
import src.constants
import numpy as np
import sys
from src.board import Board, SelectionButton, RotateButton, ShipsText, Square





def main_board_creation(screen):
    screen.fill(src.constants.BACKGROUND)
    surface = pygame.Surface(src.constants.BOARD_SIZE)
    surface.fill(src.constants.BACKGROUND)
    LEFT = 1
    RIGHT = 3
    run = True
    left_click = False
    right_click = False
    choice = 0
    while run:
        src.constants.CLOCK.tick(60)
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                left_click = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                right_click = True

        if left_click:
            cube.draw(surface)
            for selection in menu:
                if selection[1].collidepoint((mx, my)):
                    pass
        if right_click:
            cube.remove(surface)
            pass
        draw_menu(menu, screen)
        cube.update(surface.get_width() // 10)
        drawgrid(surface.get_width(), surface)
        screen.blit(surface, constants.FIRST_BOARD_POS)
        left_click, right_click = False, False
        pygame.display.flip()