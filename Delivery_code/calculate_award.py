from math import inf
def calculate_award_time(time_):
    """

    :param time_: tablica elementów (skąd, dokąd, jaki czas)
    :return: Końcowa nagroda za przejazd
    """
    sum_award = 0
    for i in time_:
        # i[2]- czas przejazdu
        award = 0
        if i[2] < 5:
            award = 40
        if i[2] < 8 and i[2] >= 5:
            award = 35
        if i[2] < 10 and i[2] >= 8:
            award = 30
        if i[2] < 15 and i[2] >= 10:
            award = 25
        if i[2] < 20 and i[2] >= 15:
            award = 20
        if i[2] < 25 and i[2] >= 20:
            award = 15
        if i[2] < 30 and i[2] >= 25:
            award = 10
        if i[2] < 40 and i[2] >= 30:
            award = 5

        sum_award += award

    return sum_award
