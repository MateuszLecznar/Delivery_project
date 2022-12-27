import math

import pygame


class Dron():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('dron.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def update_position(self, destination_x, destination_y):
        if destination_y != self.y or destination_x != self.x:
            dx = destination_x - self.x
            dy = destination_y - self.y

            angle = math.atan2(dx, dy)
            velocity = 15
            if abs(dx) > 10:
                destination_xv = math.sin(angle) * velocity
                self.x += destination_xv
            if abs(dy) > 10:
                destination_yv = math.cos(angle) * velocity
                self.y += destination_yv

    def move_dron(self, men, restaurant, road, window):
        """
        Funkcja wyznacza i ryzuje następny ruch drona
        """

        if not road:
            return None
        if road[0].isupper():
            for destination_restaurant in restaurant:
                if destination_restaurant.letter == road[0]:
                    self.update_position(destination_restaurant.x, destination_restaurant.y)
                    self.draw(window)
                    if abs(destination_restaurant.x - self.x) < 10 and abs(destination_restaurant.y - self.y) < 10:
                        road = road[1:]
                        restaurant.remove(destination_restaurant)
                        return road

        if road[0].islower():
            for destination_man in men:
                if destination_man.letter == road[0]:
                    self.update_position(destination_man.x, destination_man.y)
                    self.draw(window)
                    if abs(destination_man.x - self.x) < 10 and abs(destination_man.y - self.y) < 10:
                        road = road[1:]
                        men.remove(destination_man)
                        return road
        return road
