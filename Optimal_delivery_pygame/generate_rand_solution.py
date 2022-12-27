import copy

from Solution_Class import Solver
from calculate_award import calculate_award_time
from print_road import print_road


def first_generate():
    """
    Funkcja generuje pierwsze losowe rozwiązanie
    :return: zwraca objekt tego rozwiązania i wytyczoną drogę
    """

    object = Solver()
    road = object.create_init_solution()
    print("\nGenerowanie przykładowego rozwiązania:")
    print_road(road)
    object.check_solution(road)
    print("Nagroda przed podminą: ", calculate_award_time(object.calculate_single_delivery(copy.deepcopy(road))), "PLN")
    print_road(road)

    return object, road
