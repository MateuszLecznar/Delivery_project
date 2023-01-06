from Start_game import window
from generate_rand_solution import first_generate
import tkinter as tk
import ast


def fun():
    long_taboo = taboo.get()
    max_iter = itera.get()
    penalty = kara.get()
    penalty_iter = powtrz.get()
    try:
        max_iter = abs(int(max_iter))
        penalty = abs(int(penalty))
        penalty_iter = abs(int(penalty_iter))
        try:
            long_taboo = ast.literal_eval(long_taboo)
            for i in long_taboo:
                assert int(i) > 0
        except:
            assert int(long_taboo) > 0
        print(long_taboo, max_iter, penalty, penalty_iter)
        assert max_iter != 0
        assert penalty != 0
        assert penalty_iter != 0

    except:
        btn = tk.Button(window, text = "Wprowadź poprawne dane i spróbuj ponownie", width = 40, height = 8, command = fun, background='red')
        btn.place(x = 50, y = 110)
    else:
        btn = tk.Button(window, text="Start", width=40, height=8, command=fun, background='white')
        btn.place(x = 50, y = 110)
    window(True, long_taboo, max_iter)



if __name__ == "__main__":
    random_object_solution, road = first_generate()
    window = tk.Tk()
    window.title("Delivery")
    window.geometry("400x250")
    taboo = tk.Entry(window,width = 25)
    tabootext = tk.Label(window, text = 'Lista taboo')
    itera = tk.Entry(window,width = 10)
    itertext = tk.Label(window, text = 'Liczba iteracji')
    powtrz = tk.Entry(window,width = 10)
    powtrztext = tk.Label(window, text = 'Liczba powtórzeń kary')
    kara = tk.Entry(window,width = 10)
    karatext = tk.Label(window, text = 'Wartość kary')
    btn = tk.Button(window, text = "Start", width = 40, height = 8, command = fun, background='white')
    tabootext.place(x = 50, y = 10)
    taboo.place(x = 10, y = 35)
    itertext.place(x = 45, y = 60)
    itera.place(x = 50, y = 85)
    powtrztext.place(x = 260, y = 10)
    powtrz.place(x = 290, y = 35)
    karatext.place(x = 285, y = 60)
    kara.place(x = 290, y = 85)
    btn.place(x = 50, y = 110)
    window.mainloop()
