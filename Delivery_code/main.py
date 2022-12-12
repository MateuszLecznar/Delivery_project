import copy
import math
from math import inf
import numpy as np
import random
import sys
sys.setrecursionlimit(100)

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
                return print("Plecak przepełniony")

        time = 0
        prev_point = route[0]
        for point in route[1:]:
            time += self.cost_matrix[prev_point[0], point[0]]
            prev_point = point

        return print("Cały przejazd trwa :", time)

    def calculate_single_delivery(self, route):
        """" Funkcja zlicza czas dojazdu od danej restauracji do klienta"""
        if route[0][1].islower():  # sprawdzamy czy pierwszy punkt jest miejscem dostawy czy odbiory zamówienia( sprawdza dane wejściowe)
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

                    tuple_time.append((temp_route[0][1],temp_route[0][1].lower(), sum(single_time)))
                    single_time.clear()
                    temp_route.pop(iter)
                    temp_route.pop(0)

                    break
        return tuple_time

    def list_to_swap(self):
        """ Funkcja generuje liste możliwych wszystkich podmian potrzebną później do znalezienia najlepszej podmiany"""
        copy_restaurants=copy.deepcopy(self.restaurants)
        list_restaurant_to_swap=[]

        list_to_swap_display = []
        for rest in self.restaurants:

            for copy_rest in copy_restaurants:
                if rest[1] != copy_rest[1]:
                    list_restaurant_to_swap.append((rest[1],copy_rest[1]))
                    list_to_swap_display.append((rest[1],copy_rest[1]))
            copy_restaurants.pop(0)
            #print(list_to_swap_display)




        return list_restaurant_to_swap


    def best_change_result(self,swing_list,solution):
        """ Funkcja podmienia i przelicza czy po podmianie jest lepiej.
            Jeśli znajdzie najlepszą podmianę, podmieni i zwróci trasę i swing listę bez elementów podmiany
            return: najlepsza droga, nagroda za tą trasę, reszta możliwych podmian"""
        best_salary=0
        orginal_solution=copy.deepcopy(solution)
        best_solution=[]
        #print(swing_list)
        #print(solution)
        index_1_big=0
        index_2_big=0
        index_1_small=0
        index_2_small=0

        index_to_delate_from_swap_list=0


        for swing in swing_list:
            for i in range(len(solution)):

            #PODMIANA DUŻYCH LITER
                if solution[i][1] == swing[0]:
                    index_1_big=i

                elif solution[i][1] == swing[1]:
                    index_2_big = i

            #podmiana małych liter

                elif solution[i][1] == swing[0].lower():
                    index_1_small=i
                elif solution[i][1] == swing[1].lower():
                    index_2_small=i

            solution[index_1_big],solution[index_2_big]=solution[index_2_big],solution[index_1_big]
            solution[index_1_small], solution[index_2_small] = solution[index_2_small], solution[index_1_small]


            #porównanie nagrody
            award = print_award_time(self.calculate_single_delivery(copy.deepcopy(solution)))
            if award>best_salary:
                index_to_delate_from_swap_list=swing_list.index(swing)
                best_solution = copy.deepcopy(solution)
                best_salary=award
            #print_road(solution)
            #powrót do oryginalnych danych
            solution = copy.deepcopy(orginal_solution)

        #print_road(best_solution)
        print("Nowa nagroda: ",best_salary,"PLN")
        used_swap=swing_list.pop(index_to_delate_from_swap_list)
        print("Nastąpiła najlepsza podmiana: ",used_swap)
        return best_solution,best_salary,swing_list,used_swap

    def add_to_taboo(self,used_swap, taboo, list_to_swap):
        """ Funkcja dodaje do tablicy taboo wykonane podmiany oraz zwraca te które juz w niej były za długo"""


        taboo.append(used_swap)
        if len(taboo)>=4:  #Zmiana ile iterazji musi być w taboo podmiana
            list_to_swap.insert(0,taboo.pop(0))

        re=[]
        re.append(list_to_swap)
        re.append(taboo)
        return re
    def made_next_solution(self,a,solution,data,taboo):
        """Funcka generuje rozwiązanie i wykonuje operacje do kolejnych iteracji"""


        print(taboo)
        abc=a.add_to_taboo(data[3],taboo,data[2])

        abc[0]=data[2]
        abc[1]=taboo
        print(taboo)
        data = a.best_change_result(data[2], solution)
        a.check_solution(data[0])
        print_road(data[0])

        return a,data[0],data,taboo





def findchanges(lista):
    tab = []
    for i in lista:
        tabtab = []
        temp = 0
        if i[1].isupper() is True:
            for j in lista:
                if temp > 0 and j[1].isupper() is True:
                    tabtab.append(j)
                if j == i:
                    temp += 1
            tab.append(tabtab)
    return tab


def print_road(solution):
    for el in solution:
        if el is solution[-1]:
            print(el[1])
        else:
            print(el[1],end=" -> ")

    print("\n")
def print_award_time(time_):
    sum_award=0
    for i in time_:
        award=0
        if i[2]<5:
            award=40
        if i[2]<8 and i[2]>=5:
            award=35
        if i[2]<10 and i[2]>=8:
            award=30
        if i[2]<15 and i[2]>=10 :
            award=25
        if i[2]<20 and i[2]>=15 :
            award=20
        if i[2] < 25 and i[2] >= 20:
            award = 15
        if i[2]<30 and i[2]>=25:
            award=10
        if i[2]<40 and i[2]>=30:
            award=5
        sum_award+=award
        #print(i,"   Nagroda: ",award,"pln")
    #print("NAGRODA ZA CAŁY PRZEJAZD: ",sum_award,"pln")
    return sum_award




if __name__ == '__main__':

    a = Solver()
    solution1 = a.create_init_solution()
    print("\nGenerowanie przykładowego rozwiązania:")
    print_road(solution1)
    a.check_solution(solution1)
    print("nagroda przed podminą: ",print_award_time(a.calculate_single_delivery(copy.deepcopy(solution1))),"PLN")
    print_road(solution1)


    data=a.best_change_result(a.list_to_swap(),copy.deepcopy(solution1))
    a.check_solution(data[0])
    print_road(data[0])
    taboo=[data[3]]


    object=a
    sol=solution1
    dat_1=data
    tab=taboo
    for i in range(10):
        object,sol,dat_1,tab=a.made_next_solution(object,sol,dat_1,tab)

#Rekurencyjnie wywoływanie kolejnych powtórzeń
