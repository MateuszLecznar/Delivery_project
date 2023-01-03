# def get_letter_from_number(number):
#     """
#     Funkcja zamienia litere na cyfre od A-J
#     :param number: numer od 0-9
#     :return:
#     """
#     match number:
#         case 0:
#             return "A"
#
#         case 1:
#             return "B"
#
#         case 2:
#             return "C"
#
#         case 3:
#             return "D"
#
#         case 4:
#             return "E"
#
#         case 5:
#             return "F"
#
#         case 6:
#             return "G"
#
#         case 7:
#             return "H"
#
#         case 8:
#             return "I"
#
#         case 9:
#             return "J"
#
#         case default:
#             return False
def get_letter_from_number(number):
    """
    Funkcja zamienia litere na cyfre od A-J
    :param number: numer od 0-9
    :return:
    """
    switcher ={
        0:"A",

        1:"B",

        2: "C",

        3: "D",
        4: "E",

        5: "F",
        6: "G",

        7: "H",
        8: "I",

        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",


        }
    return switcher.get(number)