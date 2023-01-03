import math
from math import inf

import numpy as np


def create_cost_matrix(list_of_men, list_of_restaurants):
    """
    Funkcja towrzy macierz kosztów

    :param list_of_men: lista obiektów Hungry_man
    :param list_of_restaurants: Lista obiektów Restaurant_building
    :return: macierz kosztów do algorytmu taboo search
    """
    # Stworzenie odpowiedniej kolejności macierzy
    by_turns = []
    if len(list_of_men) == len(list_of_restaurants):
        for i in range(len(list_of_men)):
            by_turns.append(list_of_restaurants[i])
            by_turns.append(list_of_men[i])
    else:
        print("Różna liczba restauracji i miejsc dostawy")
        return False

    # Złożenie i oblczenie dystansów
    cost_matrix = []

    for x in by_turns:
        column = []
        for y in by_turns:

            if x.letter == y.letter and x.letter.isupper():
                column.append(inf)
            elif x.letter == y.letter and x.letter.islower():
                column.append(inf)
            elif x.letter.lower() == y.letter and x.letter.isupper():
                column.append(inf)
            else:
                column.append(int(math.dist((x.x, x.y), (y.x, y.y))))
        cost_matrix.append(column)
    return cost_matrix


def prepared_matrix(count_order, men, list_restaurant):
    """
    Funcka obrabia macierz żeby była odpowiednia do algorytmu taboo search
    :param count_order:
    :param men:
    :param list_restaurant:
    :return:
    """
    if count_order == 14:
        matrix = np.array(create_cost_matrix(men, list_restaurant))
        matrix = matrix.T
        matrix = matrix / 40  # Norlamlizuje by nie zmieniac nagród i wykorzystać funkcję do liczenia nagrody

        return matrix
    else:
        return False
