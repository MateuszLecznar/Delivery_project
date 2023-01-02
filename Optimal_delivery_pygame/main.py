from Start_game import window
from generate_rand_solution import first_generate

if __name__ == "__main__":
    random_object_solution, road = first_generate()

    long_taboo = [20, 30, 40, 50, 60, 70, 80, 90]
    max_iter = 100

    window(True, random_object_solution, road, long_taboo, max_iter)
