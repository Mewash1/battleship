import sys
from src.board_creation import main_board_creation
import src.constants
import pygame


def main():
    pygame.init()

    pygame.display.set_caption('Statki')
    text = src.constants.FONT.render('Wciśnij ENTER aby rozpocząć', True, src.constants.BLACK)
    textRect = text.get_rect()
    textRect.center = (src.constants.WIDTH/2, src.constants.HEIGHT/2)
    textRect.y += 100

    screen = pygame.display.set_mode(src.constants.SIZE)
    title_image = pygame.image.load(src.constants.BATTLESHIP).convert()
    imgrect = title_image.get_rect()
    imgrect.center = (src.constants.WIDTH/2, src.constants.HEIGHT/2)
    imgrect.y -= 80

    screen.fill(src.constants.BACKGROUND)
    screen.blit(title_image, imgrect)
    screen.blit(text, textRect)
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: main_board_creation(screen)