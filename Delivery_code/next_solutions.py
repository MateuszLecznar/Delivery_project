from generate_rand_solution import first_generate
import copy
from print_road import print_road
import matplotlib.pyplot as plt


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
    random_object_solution.next_iter_next_award=[]
    random_object_solution.lenght_taboo(length_taboo)

    list_to_swap = random_object_solution.list_to_swap_pairs()

    data = random_object_solution.best_change_result(list_to_swap, road)
    random_object_solution.check_solution(data[0])

    print_road(data[0])
    road=data[0]
    taboo = [data[3]]

    for i in range(number_of_iterations):
        random_object_solution, road, data, taboo = random_object_solution.made_next_solution(random_object_solution,
                                                                                              road, data, taboo)

    plt.plot(random_object_solution.next_iter_next_award)
    long_taboo = random_object_solution.max_taboo
    long_taboo = str(long_taboo)
    plt.title("Nagroda po kolejnych iteracjach algorytmu. Długość tablicy taboo:"+long_taboo)
    plt.show()
    print(random_object_solution.cost_matrix)