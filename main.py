import sys, pygame
import constants

def main():
    pygame.init()

    pygame.display.set_caption('Statki')
    text = constants.FONT.render('Wciśnij ENTER aby rozpocząć', True, constants.BLACK)
    textRect = text.get_rect()
    textRect.center = (constants.WIDTH/2, constants.HEIGHT/2)
    textRect.y += 100

    screen = pygame.display.set_mode(constants.SIZE)
    title_image = pygame.image.load(constants.BATTLESHIP).convert()
    imgrect = title_image.get_rect()
    imgrect.center = (constants.WIDTH/2, constants.HEIGHT/2)
    imgrect.y -= 80

    screen.fill(constants.BACKGROUND)
    screen.blit(title_image, imgrect)
    screen.blit(text, textRect)
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: sys.exit()


if __name__ == "__main__":
    main()