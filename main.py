import sys, pygame
pygame.init()

size = width, height = 1072, 603
background = 242, 216, 186
black = 0, 0, 0
font = pygame.font.SysFont('calibri', 32)
pygame.display.set_caption('Statki')
text = font.render('Wciśnij ENTER aby rozpocząć', True, black)
textRect = text.get_rect()
textRect.center = (width/2, height/2)
textRect.y += 100

screen = pygame.display.set_mode(size)
title_image = pygame.image.load("battleships.jpg").convert()
imgrect = title_image.get_rect()
imgrect.center = (width/2, height/2)
imgrect.y -= 80

screen.fill(background)
screen.blit(title_image, imgrect)
screen.blit(text, textRect)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: sys.exit()
