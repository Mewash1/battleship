import sys
from .second_screen import main_second_screen
from .constants import BLACK, WIDTH, HEIGHT, BATTLESHIP, SIZE, BACKGROUND, FONT
import pygame


def main():
    pygame.init()

    pygame.display.set_caption('Battleships')
    text = FONT.render('Press ENTER to start!', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (WIDTH/2, HEIGHT/2)
    textRect.y += 100

    screen = pygame.display.set_mode(SIZE)
    title_image = pygame.image.load(BATTLESHIP).convert()
    imgrect = title_image.get_rect()
    imgrect.center = (WIDTH/2, HEIGHT/2)
    imgrect.y -= 80

    screen.fill(BACKGROUND)
    screen.blit(title_image, imgrect)
    screen.blit(text, textRect)
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: main_second_screen(screen)