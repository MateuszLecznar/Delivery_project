from generate_rand_solution import first_generate
import copy
from print_road import print_road


def next_solution_by_iter(number_of_iterations, length_taboo):
    """
    Funkcja tworzy rozwiązanie,
    generuje listę możlwiych podmian
    iteruje zadaną liczbę razy

    :param number_of_iterations: liczba iteracji czyli podmian w algorytmie taboo
    :param length_taboo - długość tablicy taboo
    :return:
    """

    random_object_solution, road = first_generate()
    random_object_solution.lenght_taboo(length_taboo)

    list_to_swap = random_object_solution.list_to_swap_pairs()

    data = random_object_solution.best_change_result(list_to_swap, copy.deepcopy(road))
    random_object_solution.check_solution(data[0])

    print_road(data[0])
    taboo = [data[3]]

    for i in range(number_of_iterations):
        random_object_solution, road, data, taboo = random_object_solution.made_next_solution(random_object_solution,
                                                                                              road, data, taboo)
