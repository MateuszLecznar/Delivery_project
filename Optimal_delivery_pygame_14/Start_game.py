import copy
import time
import numpy as np
import pygame

import positions_restaurants
from Button_Class import Button
from Class_Hungry_man import Hungry_man
from add_restaurants import generate_restaurant
from create_cost_matrix import prepared_matrix
from display_elements import element_to_display
from move_dron import Dron
from next_solutions import next_solution_by_iter
from print_road import road_str_without_arrow,print_road
from generate_rand_solution import first_generate

def window(start,long_taboo, max_iter):
    if start:

        pygame.init()
        window = pygame.display.set_mode((1400, 1000))
        count_order = 0
        max_restaurants = 14
        men = []
        list_restaurant = generate_restaurant(True)

        out_matrix = []

        run = True
        flag_single_show = True
        flag_button_show = False

        dron = Dron(300, 300)
        road_for_dron = ""
        random_object_solution=[]
        road=[]
        while run:
            window.fill((0, 0, 0))
            # pygame.time.Clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mx, my = pygame.mouse.get_pos()
                    if count_order < max_restaurants:
                        test = Hungry_man(mx, my, count_order)
                        men.append(test)
                        count_order = count_order + 1
            time.sleep(0.03)

            best_finish_road = []

            if count_order == max_restaurants and flag_single_show:
                flag_single_show = False
                flag_button_show = True

                out_matrix = prepared_matrix(count_order, men, list_restaurant)
                random_object_solution, road = first_generate(out_matrix)
                best_salary = 0


                for el in long_taboo:
                    finish_road = road
                    best_salary_temp = []
                    finish_road, best_salary_temp = next_solution_by_iter(max_iter, el,
                                                                          copy.deepcopy(random_object_solution),
                                                                          copy.deepcopy(finish_road),
                                                                          out_matrix)
                    if best_salary < best_salary_temp:
                        best_salary = best_salary_temp
                        best_finish_road = finish_road

                road_for_dron = road_str_without_arrow(best_finish_road)
                road=best_finish_road
            element_to_display(count_order, max_restaurants, positions_restaurants, men, list_restaurant, window,road)



            if flag_button_show:

                button = Button(550, 0)
                button.draw(window)
                button.clicked = button.check_click()
                if not button.clicked:
                    road_for_dron = dron.move_dron(men, list_restaurant, road_for_dron, window)
                else:
                    dron.draw(window)

            pygame.display.update()

        for el in out_matrix.tolist():
            print(el,"\n")


        print_road(road)
        return 0
