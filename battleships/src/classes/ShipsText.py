from ..constants import BLACK, FONT


class ShipsText:
    '''
    Text for displaying how many ships are still left to be put down.
    '''
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.text = FONT.render(f"{self.value}x", True, BLACK)
        self.rect = self.text.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def draw(self, screen):
        '''
        Draws text onto the screen.
        '''
        screen.blit(self.text, self.rect)

    def update(self, new_value):
        '''
        Updates the text with a new value.
        '''
        self.value = new_value
        self.text = FONT.render(f"{self.value}x", True, BLACK)
        self.rect = self.text.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
