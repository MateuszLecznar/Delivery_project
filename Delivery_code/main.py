from next_solutions import next_solution_by_iter

"""Etap prac:
Uporządkowany kod 
generowanie rozwiązania z podmianami parami 
możliwa łatwa zmiana ilości iteracji i długości tablicy taboo 

"""

"""
PLan działania:

zaspis do pliku csv danych by:

wygenerować wykres ilości iteracji od wysokości nagrody 
wykres długości tablicy taboo od wysokości nagrody dla 100 iteracji 

"""

if __name__ == '__main__':
    """
    Parametry 
    1. Ilość iteracji 
    2. Długość tablicy taboo 
    """
    next_solution_by_iter(30, 5)
