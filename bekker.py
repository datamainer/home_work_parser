import math
import sys

LINE_LENGTH = 7


def show_sales(show_from_line=1, show_to_line=math.inf):
    if show_from_line < 2:
        show_from_position = 0
    else:
        show_from_position = (show_from_line - 1) * LINE_LENGTH

    show_to_position = show_to_line * LINE_LENGTH

    with open('bekker.txt', 'r', encoding='utf-8') as f:
        f.seek(show_from_position)
        line = f.readline()
        while line:
            print(line.strip())
            if show_to_position < f.tell():
                break
            line = f.readline()


show_sales()