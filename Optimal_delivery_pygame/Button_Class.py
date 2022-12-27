import pygame


class Button():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('button.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.letters = "NACIŚNIJ BY ZATRZYMAĆ"
        self.clicked = False

    def draw(self, window):

        window.blit(self.image, (self.rect.x, self.rect.y))

        my_font = pygame.font.SysFont('Comic Sans MS', 23)
        text = my_font.render(self.letters, False, (255, 255, 0))
        window.blit(text, (self.x + 50, self.y + 55))

    def check_click(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True

        return False
