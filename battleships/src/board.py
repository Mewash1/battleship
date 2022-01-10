import pygame
import src.constants


class Board:
    def __init__(self, board_size, board_pos) -> None:
        self.board_size = board_size
        self.surface = pygame.Surface(board_size)
        self.surface.fill(src.constants.BACKGROUND)
        self.board_pos = board_pos
        self.square_size = self.board_size[0] // 10 
    
    def draw_board(self):
        for i in range(0, self.board_size[0] + 1, self.square_size):
            x, y = i, i
            pygame.draw.line(self.surface, (255, 255, 255), (x, 0), (x, self.board_size[0]), 4)
            pygame.draw.line(self.surface, (255, 255, 255), (0, y), (self.board_size[0], y), 4)

    def draw_ship(self, ship_type):
        ship_type.draw()


class ShipsText:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.text = src.constants.FONT.render(f"{self.value}x", True, src.constants.BLACK)
        self.rect = self.text.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def draw(self, screen):
        screen.blit(self.text, self.rect)

    def update(self, new_value):
        self.value = new_value
        self.text = src.constants.FONT.render(f"{self.value}x", True, src.constants.BLACK)
        self.rect = self.text.get_rect()
    

class Button:
    def __init__(self, picture, x, y, is_clickable, is_clicked, clicked_picture) -> None:
        self.picture = picture
        self.clicked_picture = clicked_picture
        self.x = x
        self.y = y
        self.is_clikable = is_clickable
        self.is_clicked = is_clicked
        self.update()
    
    def draw(self, screen):
        screen.blit(self.current_picture, self.rect)

    def update(self):
        if self.is_clicked:
            self.current_picture = pygame.image.load(self.clicked_picture).convert()
        else:
            self.current_picture = pygame.image.load(self.picture).convert()
        self.rect = self.current_picture.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class SelectionButton(Button):
    def __init__(self, picture, x, y, is_clickable, is_clicked, clicked_picture, ship_type) -> None:
        super().__init__(picture, x, y, is_clickable, is_clicked, clicked_picture)
        self.ship_type = ship_type


class RotateButton(Button):
    def __init__(self, picture, x, y, is_clickable, is_clicked, clicked_picture) -> None:
        super().__init__(picture, x, y, is_clickable, is_clicked, clicked_picture)
        self.rotaion_table = {1: 5, 2: 6, 3: 7, 4: 8}

    def hori_to_verti(self, ship_type):
        return self.rotaion_table[ship_type]
    
    def verti_to_hori(self, ship_type):
        for key, value in self.rotaion_table.items():
            if value == ship_type:
                return key


class Square:
    def __init__(self, square_size, height_factor, width_factor):
        self.height = square_size * height_factor
        self.width = square_size * width_factor
        self.square_size = square_size

    def update(self, board_pos):
        x, y = pygame.mouse.get_pos()
        x, y = x - board_pos[0], y - board_pos[1]
        ix = x // self.square_size
        iy = y // self.square_size
        self.cx, self.cy = ix * self.square_size, iy * self.square_size
        self.square = pygame.Rect(self.cx, self.cy, self.height, self.width)
        print(self.cx/35, self.cy/35)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.square)

    def remove(self, surface):
        pygame.draw.rect(surface, src.constants.BACKGROUND, self.square)
    
    