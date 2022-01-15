from ..constants import BACKGROUND, BLACK, FONT


class ShipsText:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.text = FONT.render(f"{self.value}x", True, BLACK)
        self.rect = self.text.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def draw(self, screen):
        screen.blit(self.text, self.rect)

    def update(self, new_value):
        self.value = new_value
        self.text = FONT.render(f"{self.value}x", True, BLACK)
        self.rect = self.text.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
    
    def erase(self):
        self.text = FONT.render(f"{self.value}x", True, BACKGROUND)