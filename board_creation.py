import pygame
import constants
import numpy as np
import sys


class ShipSelection():
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.text = constants.FONT.render(f"{self.value}x", True, constants.BLACK)
        self.rect = self.text.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def draw_selection(self, screen):
        screen.blit(self.text, self.rect)

    def update(self, new_value):
        self.value = new_value
        self.text = constants.FONT.render(f"{self.value}x", True, constants.BLACK)
        self.rect = self.text.get_rect()
    

def gen_menu():
    four_selection = ShipSelection(1, constants.TEXT_POS[0], constants.TEXT_POS[1])
    three_selection = ShipSelection(2, constants.TEXT_POS[0], constants.TEXT_POS[1] + 100)
    two_selection = ShipSelection(3, constants.TEXT_POS[0], constants.TEXT_POS[1] + 200)
    one_selection = ShipSelection(4, constants.TEXT_POS[0], constants.TEXT_POS[1] + 300)

    button_4 = pygame.Rect(four_selection.x + 50, four_selection.y, 4 * (constants.BOARD_SIZE[0] // 10), constants.BOARD_SIZE[0] // 10)
    button_3 = pygame.Rect(three_selection.x + 50, three_selection.y, 3 * (constants.BOARD_SIZE[0] // 10), constants.BOARD_SIZE[0] // 10)
    button_2 = pygame.Rect(two_selection.x + 50, two_selection.y, 2 * (constants.BOARD_SIZE[0] // 10), constants.BOARD_SIZE[0] // 10)
    button_1 = pygame.Rect(one_selection.x + 50, one_selection.y, 1 * (constants.BOARD_SIZE[0] // 10), constants.BOARD_SIZE[0] // 10)

    menu_list = [(four_selection, button_4), 
    (three_selection, button_3),
    (two_selection, button_2),
    (one_selection, button_1)]

    return menu_list


def draw_menu(menu, screen):
    for selection in menu:
        selection[0].draw_selection(screen)
        pygame.draw.rect(screen, (255, 255, 255), selection[1])


def drawgrid(w, surface):
    sizebtwn = w // 10 
    for i in range(0, w+1, sizebtwn):
        x, y = i, i
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w), 4)
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y), 4)



def main_board_creation(screen):
    screen.fill(constants.BACKGROUND)
    surface = pygame.Surface(constants.BOARD_SIZE)
    surface.fill(constants.BACKGROUND)
    LEFT = 1
    RIGHT = 3
    cube = Cube()
    run = True
    left_click = False
    right_click = False
    choice = 0
    menu = gen_menu()
    while run:
        constants.CLOCK.tick(60)
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