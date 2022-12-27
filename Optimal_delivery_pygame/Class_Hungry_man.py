import pygame

from add_restaurants import get_letter_from_number


class Hungry_man:

    def __init__(self, x, y, number_of_order):
        self.x = x - 25
        self.y = y - 25
        self.width = 0
        self.height = 0
        self.image = pygame.image.load('hungry-man-cartoon.png')

        self.letter = get_letter_from_number(number_of_order).lower()

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text = my_font.render(self.letter, False, (255, 255, 255))
        window.blit(text, (self.x + 30, self.y - 30))
