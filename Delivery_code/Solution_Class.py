import copy
from math import inf
import numpy as np
import random
from print_road import print_road
from calculate_award import calculate_award_time
from Order_Class import Order


class Solver:
    """
    Klasa naszego rozwiązania
    """
    cost_matrix = np.array(

        [[inf, 3, 10, 6, 2, 7, 3, 10, 9, 4, 2, 3, 10, 9, 8, 10, 4, 6, 5, 6],
         [inf, inf, 10, 6, 5, 6, 1, 8, 1, 4, 3, 4, 1, 5, 2, 3, 5, 8, 9, 1],
         [10, 10, inf, 3, 4, 7, 7, 7, 6, 2, 10, 1, 6, 7, 4, 6, 1, 5, 2, 3],
         [6, 6, inf, inf, 7, 5, 7, 1, 5, 9, 4, 8, 7, 9, 8, 10, 9, 1, 6, 5],
         [2, 5, 4, 7, inf, 10, 10, 6, 3, 9, 7, 2, 8, 3, 5, 8, 6, 5, 4, 9],
         [7, 6, 7, 5, inf, inf, 10, 7, 3, 8, 6, 8, 8, 3, 8, 6, 9, 4, 8, 2],
         [3, 1, 7, 7, 10, 10, inf, 5, 1, 1, 7, 10, 1, 4, 9, 7, 3, 2, 1, 1],
         [10, 8, 7, 1, 6, 7, inf, inf, 7, 1, 1, 5, 4, 2, 9, 4, 4, 5, 10, 2],
         [9, 1, 6, 5, 3, 3, 1, 7, inf, 8, 9, 4, 1, 7, 4, 10, 6, 8, 6, 7],
         [4, 4, 2, 9, 9, 8, 1, 1, inf, inf, 10, 10, 7, 10, 6, 4, 1, 7, 8, 10],
         [2, 3, 10, 4, 7, 6, 7, 1, 9, 10, inf, 6, 8, 1, 5, 9, 2, 3, 3, 7],
         [3, 4, 1, 8, 2, 8, 10, 5, 4, 10, inf, inf, 5, 7, 9, 9, 9, 6, 6, 5],
         [10, 1, 6, 7, 8, 8, 1, 4, 1, 7, 8, 5, inf, 10, 3, 9, 7, 6, 2, 8],
         [9, 5, 7, 9, 3, 3, 4, 2, 7, 10, 1, 7, inf, inf, 9, 7, 9, 8, 2, 4],
         [8, 2, 4, 8, 5, 8, 9, 9, 4, 6, 5, 9, 3, 9, inf, 5, 1, 2, 8, 4],
         [10, 3, 6, 10, 8, 6, 7, 4, 10, 4, 9, 9, 9, 7, inf, inf, 9, 3, 3, 1],
         [4, 5, 1, 9, 6, 9, 3, 4, 6, 1, 2, 9, 7, 9, 1, 9, inf, 10, 4, 8],
         [6, 8, 5, 1, 5, 4, 2, 5, 8, 7, 3, 6, 6, 8, 2, 3, inf, inf, 7, 8],
         [5, 9, 2, 6, 4, 8, 1, 10, 6, 8, 3, 6, 2, 2, 8, 3, 4, 7, inf, 6],
         [6, 1, 3, 5, 9, 2, 1, 2, 7, 10, 7, 5, 8, 4, 4, 1, 8, 8, inf, inf]]
    )
    backpack_volume = 3
    max_taboo = 23

    def lenght_taboo(self, lenght_taboo):
        self.max_taboo = lenght_taboo

    restaurants = [Order.A, Order.B, Order.C, Order.D, Order.E, Order.F, Order.G, Order.H, Order.I,
                   Order.J]  # przypisanie restauracji
    customers = [Order.a, Order.b, Order.c, Order.d, Order.e, Order.f, Order.g, Order.h, Order.i,
                 Order.j]  # przypisanie klientów

    def create_init_solution(self):
        """
        Funkcja generuje przykładowe rozwiazanie które jest możliwe ale nie koniecznie jest optymalne (raczej napewno nie będzie bo oparta na liczbie losowej)


        :return: wektor możliwej drogi prezbytej przez kuriera
        """

        c_order = self.restaurants[:]
        d_order = self.customers[:]
        start_point = 0  # random.randint(0, len(c_order) - 1)

        x_init = [c_order[start_point]]

        backpack = [d_order[start_point]]  # włożenie pierwszego zamówienia do plecaka

        c_order.remove(c_order[start_point])
        d_order.remove(d_order[start_point])

        while len(x_init) != len(
                self.restaurants + self.customers):  # dopóki są zamówienia do odebrania lub do dostarczenia wykonuj

            if len(backpack) < self.backpack_volume:  # jeśli ilosc w plecaku < pojemnosci plecaka wykonaj:
                # dodanie restauracji albo towaru do plecaka
                if random.randint(0, 1) == 0:  # restauracji
                    if c_order:
                        next_point = 0
                        if len(c_order) > 1:
                            next_point = random.randint(0, len(c_order) - 1)
                        x_init.append(c_order[next_point])
                        backpack.append(d_order[next_point])
                        c_order.remove(c_order[next_point])
                        d_order.remove(d_order[next_point])
                elif backpack:  # tutaj dodamy do sciezki klienta
                    next_point = 0
                    if len(backpack) > 1:
                        next_point = random.randint(0,
                                                    len(backpack) - 1)  # wylosowanie do którego klienta z wzietych zamówien jedziemy
                    x_init.append(backpack[next_point])
                    backpack.remove(backpack[next_point])

            else:  # musimy dodac do sciezki klienta bo plecak jest pelny
                next_point = random.randint(0, len(backpack) - 1)
                x_init.append(backpack[next_point])
                backpack.remove(backpack[next_point])
        return x_init

    def check_solution(self, route):
        """
        Funkcja zliczająca czas na cały przejazd oraz sprwdza czy aktualnie w plecaku jest makxymalnie 3 zamówienia
        """
        if route[0][1].islower():  # sprawdzamy czy pierwszy punkt jest miejscem dostawy czy odbiory zamówienia
            return False
        else:
            tmp = [route[0]]

        for el in route[1:]:
            if el[1].islower() and (el[0] - 1, el[1].upper()) not in tmp:
                return False
            elif el[1].isupper():
                tmp.append(el)

        backpack = 0
        for el in route:
            if el[1].isupper():
                backpack += 1
            else:
                backpack -= 1
            if backpack > self.backpack_volume:
                return False

        time = 0
        prev_point = route[0]
        for point in route[1:]:
            time += self.cost_matrix[prev_point[0], point[0]]
            prev_point = point

        return print("Cały przejazd trwa :", time)

    def calculate_single_delivery(self, route):
        """
        Funkcja zlicza czas dojazdu od danej restauracji do klienta
        :param route: droga w postaci tablicy elementów z indeksem restauracji/punktu odbioru
        :return: tablica skąd dokąd i jak długo będzie trwała podróż
        """
        if route[0][
            1].islower():  # sprawdzamy czy pierwszy punkt jest miejscem dostawy czy odbiory zamówienia( sprawdza dane wejściowe)
            return False
        temp_route = route
        single_time = []
        tuple_time = []

        while (temp_route):

            iter = 1
            while True:
                if temp_route[iter][1] != temp_route[0][1].lower():
                    single_time.append(self.cost_matrix[temp_route[0][0], temp_route[iter][0]])

                    iter += 1

                elif temp_route[iter][1] == temp_route[0][1].lower():

                    single_time.append(self.cost_matrix[temp_route[0][0], temp_route[iter][0]])

                    tuple_time.append((temp_route[0][1], temp_route[0][1].lower(), sum(single_time)))
                    single_time.clear()
                    temp_route.pop(iter)
                    temp_route.pop(0)

                    break
        return tuple_time

    def list_to_swap_pairs(self):
        """
        Funkcja generuje liste możliwych wszystkich podmian potrzebną później do znalezienia najlepszej podmiany
        :return: lista par do możliwej podmiany
        """
        copy_restaurants = copy.deepcopy(self.restaurants)
        list_restaurant_to_swap = []

        list_to_swap_pairs_display = []
        for rest in self.restaurants:

            for copy_rest in copy_restaurants:
                if rest[1] != copy_rest[1]:
                    list_restaurant_to_swap.append((rest[1], copy_rest[1]))
                    list_to_swap_pairs_display.append((rest[1], copy_rest[1]))
            copy_restaurants.pop(0)
            # print(list_to_swap_pairs_display)

        return list_restaurant_to_swap

    def best_change_result(self, swing_list, solution):
        """
                Funkcja podmienia i przelicza czy po podmianie jest lepiej.
            Jeśli znajdzie najlepszą podmianę, podmieni i zwróci trasę i swing listę bez elementów podmiany


        :param swing_list: lista możliwych podmian
        :param solution: nasza droga jaką obecnie mamy wyznaczoną
        :return: najlepsza droga, nagroda za tą trasę, reszta możliwych podmian, użyta podmiana
        """

        best_salary = 0
        orginal_solution = copy.deepcopy(solution)
        best_solution = []
        index_1_big = 0
        index_2_big = 0
        index_1_small = 0
        index_2_small = 0

        index_to_delate_from_swap_list = 0

        for swing in swing_list:
            for i in range(len(solution)):

                # PODMIANA DUŻYCH LITER
                if solution[i][1] == swing[0]:
                    index_1_big = i

                elif solution[i][1] == swing[1]:
                    index_2_big = i

                # podmiana małych liter

                elif solution[i][1] == swing[0].lower():
                    index_1_small = i
                elif solution[i][1] == swing[1].lower():
                    index_2_small = i

            solution[index_1_big], solution[index_2_big] = solution[index_2_big], solution[index_1_big]
            solution[index_1_small], solution[index_2_small] = solution[index_2_small], solution[index_1_small]

            # porównanie nagrody
            award = calculate_award_time(self.calculate_single_delivery(copy.deepcopy(solution)))
            if award > best_salary:
                index_to_delate_from_swap_list = swing_list.index(swing)
                best_solution = copy.deepcopy(solution)
                best_salary = award

            solution = copy.deepcopy(orginal_solution)

        print("Nowa nagroda: ", best_salary, "PLN")
        used_swap = swing_list.pop(index_to_delate_from_swap_list)
        print("Nastąpiła najlepsza podmiana: ", used_swap)
        return best_solution, best_salary, swing_list, used_swap

    def add_to_taboo(self, used_swap, taboo, list_to_swap_pairs):
        """
        !!!!!!!!!!!!!!!!!!!!! UWAGA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        W tej funkcji ustala się długość listy taboo

        Funkcja dodaje do tablicy taboo wykonane podmiany oraz zwraca te które juz w niej były za długo

        :param used_swap: użyta podmiana
        :param taboo: obezna lista taboo
        :param list_to_swap_pairs: lista par które możemy podmienić
        Ważne Lisa możliwych podmian jest już bez used_swap

        :return: new_taboo_and_list_to_swap -KROTKA: nowa lista taboo po aktualizacji (dodanie nowegio elementu i ewentualne wyrzucenie starego i lista możwliwych podmian

        """

        new_taboo_and_list_to_swap = []
        if taboo[0] == used_swap:
            new_taboo_and_list_to_swap.append(taboo)
        else:
            taboo.append(used_swap)
            new_taboo_and_list_to_swap.append(taboo)

        if len(taboo) >= self.max_taboo:  # Zmiana ile iterazji musi być w taboo podmiana
            list_to_swap_pairs.insert(0, taboo.pop(0))

        new_taboo_and_list_to_swap.append(list_to_swap_pairs)

        return new_taboo_and_list_to_swap

    def made_next_solution(self, object, solution, data, taboo):
        """Funcka generuje rozwiązanie i wykonuje operacje do kolejnych iteracji"""
        """ data - > best_solution,best_salary,swing_list,used_swap"""

        # Tu się dzieją czary nie wiem dlaczego ale działa

        object.add_to_taboo(data[3], taboo, data[2])

        # abc[1]=data[2]
        # abc[0]=taboo

        print("Aktualna tablica taboo: ", taboo)

        data = object.best_change_result(data[2], solution)
        object.check_solution(data[0])
        print_road(data[0])

        return object, data[0], data, taboo
