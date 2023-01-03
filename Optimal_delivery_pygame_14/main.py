from Start_game import window
from generate_rand_solution import first_generate

if __name__ == "__main__":


    long_taboo = [ 5,10,40,70, 80, 90]
    max_iter = 400

    window(True, long_taboo, max_iter)
