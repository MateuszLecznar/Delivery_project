import pygame

from print_road import road_str


def element_to_display(count_order, max_restaurants, positions_restaurants, men, list_restaurant, window, solution=None):
    """

    :param count_order:
    :param max_restaurants:
    :param positions_restaurants:
    :param men:
    :param list_restaurant:
    :param window:
    :return:
    """

    if count_order < max_restaurants:
        my_font = pygame.font.SysFont('Comic Sans MS', 60)
        current_count_text = my_font.render(
            'Wybierz miejsce dostawy dla restauracji  ' + positions_restaurants.get_letter_from_number(
                count_order), False, (220, 0, 0))
        window.blit(current_count_text, (500, 0))
    elif solution==None:
        my_font = pygame.font.SysFont('Comic Sans MS', 60)
        current_count_text = my_font.render(
            ' Tworzenie najbardziej zarobkowej drogi '
                , False, (220, 0, 0))
        window.blit(current_count_text, (500, 0))

    if count_order == max_restaurants and solution is not None:
        road_string = road_str(solution)

        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        current_count_text = my_font.render(road_string
                                            , False, (220, 0, 0))
        window.blit(current_count_text, (10, 0))



    for el in men:
        el.draw(window)

    for el in list_restaurant:
        el.draw(window)
