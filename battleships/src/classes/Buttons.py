import pygame


class Button:
    '''
    General Button class. Every object has two pictures - for clicked state and not clicked state. \n
    Before drawing the button onto the screen it is crucial to update it first.
    '''
    def __init__(self, picture, x, y, is_clicked, clicked_picture) -> None:
        self.picture = picture
        self.clicked_picture = clicked_picture
        self.x = x
        self.y = y
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
    '''
    Subclass of Button. Comes with one extra variable: ship_type, that is used for displaying text correctly.
    '''
    def __init__(self, picture, x, y, is_clicked, clicked_picture, ship_type) -> None:
        super().__init__(picture, x, y, is_clicked, clicked_picture)
        self.ship_type = ship_type


class RotateButton(Button):
    '''
    Subclass of Button. It can convert horizontal ships to vertical ones and vice versa.
    '''
    def __init__(self, picture, x, y, is_clicked, clicked_picture) -> None:
        super().__init__(picture, x, y, is_clicked, clicked_picture)
        self.rotaion_table = {1: 5, 2: 6, 3: 7, 4: 8}

    def hori_to_verti(self, ship_type):
        return self.rotaion_table[ship_type]
    
    def verti_to_hori(self, ship_type):
        for key, value in self.rotaion_table.items():
            if value == ship_type:
                return key


class SubmitButton(Button):
    '''
    Subclass of Button. It can be turned on and off by modifying the is_clickable variable.\n
    It also doesn't need a second picture.
    '''
    def __init__(self, picture, x, y, is_clicked, clicked_picture) -> None:
        super().__init__(picture, x, y, is_clicked, clicked_picture)
        self.picture = pygame.image.load(self.picture).convert()
        self.rect = self.picture.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.is_clickable = False
    
    def update(self):
        return None

    def draw(self, screen):
        screen.blit(self.picture, self.rect)
