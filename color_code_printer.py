# This file pritns the color code manual
import color_code_handler
from constants import NUMBER_OF_PAIRS


def print_color_code_manual():
    row_format = "{:>15}" * (3)
    table_headers = ["Pair number", "Major Color", "Minor Color"]
    print(row_format.format("","25-Pair Color Code",""))
    print(row_format.format(*table_headers))
    for i in range(1, NUMBER_OF_PAIRS):
        color_pair = color_code_handler.get_color_from_pair_number(i)
        print(row_format.format(i, *color_pair))

if __name__ == '__main__':
    print_color_code_manual()
