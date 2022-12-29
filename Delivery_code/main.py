import copy

from next_solutions import next_solution_by_iter
from generate_rand_solution import first_generate

"""Etap prac:
Uporządkowany kod 
generowanie rozwiązania z podmianami parami
możliwa łatwa zmiana ilości iteracji i długości tablicy taboo 

"""

"""
PLan działania:

zrobnić podmianę pojedyńczych elementów 
"""

if __name__ == '__main__':


    """
    Parametry 
    1. Ilość iteracji 
    2. Długość tablicy taboo 
    """
    """ Dla jednego """
    next_solution_by_iter(100, 40)
    next_solution_by_iter(100,20)
    next_solution_by_iter(100, 10)
    next_solution_by_iter(100, 5)
