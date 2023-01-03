import pygame

from positions_restaurants import get_letter_from_number


class Restaurant_building:

    def __init__(self, x, y, number):
        self.x = x - 40
        self.y = y - 40
        self.width = 0
        self.height = 0
        self.image = pygame.image.load('restaurant.png')
        self.letter = get_letter_from_number(number)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text = my_font.render(self.letter, False, (255, 255, 255))
        window.blit(text, (self.x + 30, self.y - 30))


def generate_restaurant(my_points):
    """
    Na sztywno wpisana lokalizacja restauracji

    :param my_points: jeśli true to generuja sie na sztuwno przypisane lokalizacje restauracji
    :return: lista obeiktów restauracja
    """

    if my_points:
        list_of_restaurants = []
        list_of_restaurants.append(Restaurant_building(100, 200, 0))
        list_of_restaurants.append(Restaurant_building(1100, 900, 1))
        list_of_restaurants.append(Restaurant_building(300, 100, 2))
        list_of_restaurants.append(Restaurant_building(1000, 600, 3))
        list_of_restaurants.append(Restaurant_building(700, 500, 4))
        list_of_restaurants.append(Restaurant_building(600, 800, 5))
        list_of_restaurants.append(Restaurant_building(1200, 200, 6))
        list_of_restaurants.append(Restaurant_building(900, 200, 7))
        list_of_restaurants.append(Restaurant_building(300, 500, 8))
        list_of_restaurants.append(Restaurant_building(1300, 800, 9))
        list_of_restaurants.append(Restaurant_building(1040, 400, 10))
        list_of_restaurants.append(Restaurant_building(550, 700, 11))
        list_of_restaurants.append(Restaurant_building(1300, 100, 12))
        list_of_restaurants.append(Restaurant_building(300, 800, 13))
        return list_of_restaurants
