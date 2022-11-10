from math import inf
import numpy as np
import random
"""
Etap prac: Przygotowanie danych, generowanie przykładowego rozwiązania spełniającego warunek 3 zamówień w plecaku. 
"""


class Order():
    """
    Duża litera- restauracja
    mała litera- punkt odbiory z restauracji o tej samej literze (tylko dużej)
    pierwsze miejsce w krotce liczba jeśli parzysta to punkt Odbioru jeśli nieparzysta punkt dostawy
    """
    A = (0, 'A')
    a = (1, 'a')
    B = (2, 'B')
    b = (3, 'b')
    C = (4, 'C')
    c = (5, 'c')
    D = (6, 'D')
    d = (7, 'd')
    E = (8, 'E')
    e = (9, 'e')
    F = (10, 'F')
    f = (11, 'f')
    G = (12, 'G')
    g = (13, 'g')
    H = (14, 'H')
    h = (15, 'h')
    I = (16, 'I')
    i = (17, 'i')
    J = (18, 'J')
    j = (19, 'j')


class Solver:
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
    restaurants = [Order.A, Order.B, Order.C, Order.D, Order.E, Order.F, Order.G, Order.H, Order.I, Order.J] #przypisanie restauracji
    customers = [Order.a, Order.b, Order.c, Order.d, Order.e, Order.f, Order.g, Order.h, Order.i, Order.j] #przypisanie klientów

    def create_init_solution(self):
        """
        Funkcja generuje przykładowe rozwiazanie które jest możliwe ale nie koniecznie jest optymalne (raczej napewno nie będzie bo oparta na liczbie losowej)


        :return: wektor możliwej drogi prezbytej przez kuriera
        """

        c_order = self.restaurants[:]
        d_order = self.customers[:]
        start_point = 0                            #random.randint(0, len(c_order) - 1)
        x_init = [c_order[start_point]]

        backpack = [d_order[start_point]] # włożenie pierwszego zamówienia do plecaka

        c_order.remove(c_order[start_point])
        d_order.remove(d_order[start_point])


        while len(x_init) != len(self.restaurants + self.customers):  # dopóki są zamówienia do odebrania lub do dostarczenia wykonuj

            if len(backpack) < self.backpack_volume:  # jeśli ilosc w plecaku < pojemnosci plecaka wykonaj:
                # dodanie restauracji albo towaru do plecaka
                if random.randint(0, 1) == 0: #restauracji
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
                        next_point = random.randint(0, len(backpack) - 1)
                    x_init.append(backpack[next_point])
                    backpack.remove(backpack[next_point])

            else:  # musimy dodac do sciezki klienta bo plecak jest pelny
                next_point = random.randint(0, len(backpack) - 1)
                x_init.append(backpack[next_point])
                backpack.remove(backpack[next_point])
        return x_init


if __name__ == '__main__':
    """
    Przykładowa droga dostawcy, mimo że zaczyna z tego samego punktu droga jest inna ponieważ bazuje na losowości.
    """
    a=Solver()
    print(a.create_init_solution())
    print(a.create_init_solution())
    print(a.create_init_solution())
