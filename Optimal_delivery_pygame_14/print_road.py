def print_road(solution):
    """
    Funkcja wypisuje trasę w widoczny sposób
    :param solution: trasa naszego kuriera
    :return:
    """

    for el in solution:
        if el is solution[-1]:
            print(el[1])

        else:
            print(el[1], end=" -> ")

    print("\n")


def road_str(solution):
    """
    Funkcja wypisuje trasę w widoczny sposób
    :param solution: trasa naszego kuriera
    :return:string trasy
    """
    road_string = ""
    for el in solution:
        if el is solution[-1]:

            road_string += el[1]
        else:

            road_string += el[1] + " -> "

    return road_string


def road_str_without_arrow(solution):
    """
    Funkcja wypisuje trasę w widoczny sposób
    :param solution: trasa naszego kuriera
    :return:string trasy
    """
    road_string = ""
    for el in solution:
        road_string += el[1]

    return road_string


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
