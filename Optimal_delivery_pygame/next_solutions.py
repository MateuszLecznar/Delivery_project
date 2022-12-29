import copy

import matplotlib.pyplot as plt
import numpy as np

from print_road import print_road


def next_solution_by_iter(number_of_iterations, length_taboo, random_object_solution, road, new_cost_matrix=None,
                          enought=None):
    """
    Funkcja tworzy rozwiązanie,
    generuje listę możlwiych podmian
    iteruje zadaną liczbę razy

    :param number_of_iterations: długość tablicy taboo
    :param length_taboo - długość tablicy taboo
    :return:
    """

    random_object_solution.next_iter_next_award = []

    if isinstance(new_cost_matrix, np.ndarray):
        random_object_solution.cost_matrix = new_cost_matrix

    random_object_solution.lenght_taboo(length_taboo)
    list_to_swap = random_object_solution.list_to_swap_pairs()

    #Generowanie pierwszego rozwiązania
    data = random_object_solution.best_change_result(list_to_swap, road)
    random_object_solution.check_solution(data[0])

    print_road(data[0])
    road = data[0]
    taboo = [data[3]]
    best_salary = 0
    best_road = []
    minimium_iteration = 0
    for i in range(number_of_iterations):



        "Tutaj implementacja kolejnych funkcji podmian pojedyńczych "





        random_object_solution, road, data, taboo = random_object_solution.made_next_solution(random_object_solution,
                                                                                              road, data, taboo)

        if best_salary < data[1]:
            best_salary = data[1]
            best_road = copy.deepcopy(road)
            minimium_iteration = i

    plt.plot(random_object_solution.next_iter_next_award)
    long_taboo = random_object_solution.max_taboo
    long_taboo = str(long_taboo)
    plt.title("Nagroda po kolejnych iteracjach algorytmu. Długość tablicy taboo:" + long_taboo)
    plt.xlabel("Numer iteracji")
    plt.ylabel("Uzyskana nagroda w PLN")
    plt.show()
    # print(random_object_solution.cost_matrix)
    print("NAJLEPSZE ROZWIĄZANIE UZYSKANO PO ", minimium_iteration + 1, " ITERACJACH DLA DŁUGOŚĆI TABLICY TABOO ",
          length_taboo, "UZYSKANA NAGRODA: ", best_salary)
    return best_road, best_salary
