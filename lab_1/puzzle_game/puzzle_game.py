"""
My version of "Puzzle game" board validation on GitHub:
https://github.com/bmykhaylivvv/coding_semester_2/tree/main/lab_1/puzzle_game
"""

# board for doctests
board = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  82  *",
    "3   2  **",
    "  8  1***",
    "  2  ****"
]


def remove_stars(char):
    if char != '*' and char != ' ':
        return True
    else:
        return False


def numeric_check(colors):
    """
    Function checks if each element in list is str(number) or blank character
    >>> numeric_check([[' ', ' ', '3', ' ', ' ', ' ', '2', ' ', ' '],\
                       [' ', ' ', '6', ' ', ' ', '8', ' ', ' ', '1'],\
                       [' ', '4', ' ', ' ', ' ', ' ', '2', ' ', ' '],\
                       ['1', ' ', ' ', ' ', ' ', '8', '2', ' ', ' '],\
                       [' ', ' ', '3', '1', ' ', '9', ' ', '5', ' ']])
    True
    """
    numbers_plus_blank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    for color in colors:
        for char in color:
            if char not in numbers_plus_blank:
                return False
    return True


def horizontal_lines(board):
    """
    Function reads horizontal lines on the board
    >>> horizontal_lines(board)
    [['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '2', ' ', ' ', '*'], ['3', ' ', ' ', ' ', '2', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '1', '*', '*', '*'], [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]
    """
    horizontals = []
    for line in board:
        line_list = list(line)
        horizontals.append(line_list)
    return horizontals


def vertical_lines(board):
    """
    Function reads vertical lines on the board
    >>> vertical_lines(board)
    [['*', '*', '*', '*', ' ', ' ', '3', ' ', ' '], ['*', '*', '*', ' ', ' ', '6', ' ', ' ', ' '], ['*', '*', ' ', '4', ' ', ' ', ' ', '8', '2'], ['*', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', '3', '1', ' ', '8', '2', ' ', ' '], ['*', '*', '*', '*', '9', '2', ' ', '1', '*'], ['*', '*', '*', '*', ' ', ' ', ' ', '*', '*'], ['*', '*', '*', '*', '5', ' ', '*', '*', '*'], ['*', '*', '*', '*', ' ', '*', '*', '*', '*']]
    """
    verticals = []
    column = []
    for position in range(len(board)):
        for row in board:
            column.append(row[position])
        verticals.append(column)
        column = []
    return verticals


def one_color(board):
    """
    Function reads sections with the same color on the boards
    >>> one_color(board)
    [[' ', ' ', '3', ' ', ' ', ' ', '2', ' ', ' '], [' ', ' ', '6', ' ', ' ', '8', ' ', ' ', '1'], [' ', '4', ' ', ' ', ' ', ' ', '2', ' ', ' '], ['1', ' ', ' ', ' ', ' ', '8', '2', ' ', ' '], [' ', ' ', '3', '1', ' ', '9', ' ', '5', ' ']]
    """
    same_color = []
    vertical = []
    for i in range(5):
        vertical.append(vertical_lines(board)[i][(4 - i):(9 - i)])

    horizontal = []
    for j in range(5):
        horizontal.append(horizontal_lines(board)[8 - j][(1 + j):(5 + j)])

    for k in range(len(vertical)):
        same_color.append(vertical[k] + horizontal[k])

    return same_color


def repeat_check(lst):
    """
    Fuction checks if there are repeatable characters in rows, columns or 
    sections with the same color
    >>> repeat_check([['*', '*', '*', '*', ' ', ' ', '3', ' ', ' '],\
                      ['*', '*', '*', ' ', ' ', '6', ' ', ' ', ' '],\
                      ['*', '*', ' ', '4', ' ', ' ', ' ', '8', '2'],\
                      ['*', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                      [' ', ' ', '3', '1', ' ', '8', '2', ' ', ' '],\
                      ['*', '*', '*', '*', '9', '2', ' ', '1', '*'],\
                      ['*', '*', '*', '*', ' ', ' ', ' ', '*', '*'],\
                      ['*', '*', '*', '*', '5', ' ', '*', '*', '*'],\
                      ['*', '*', '*', '*', ' ', '*', '*', '*', '*']])
    True
    """
    new_lines = []
    for line in lst:
        new_line = list(filter(remove_stars, line))
        new_lines.append(new_line)

    for ln in new_lines:
        if len(ln) != len(set(ln)):
            return False
    return True


def validate_board(board):
    """
    MAIN FUNCTION
    Function checks if board is valid for game
    >>> validate_board(board)
    True
    """

    if repeat_check(horizontal_lines(board)) and repeat_check(vertical_lines(board))\
            and repeat_check(one_color(board)+vertical_lines(board)+horizontal_lines(board)) and numeric_check(one_color(board)):
        return True
    return False


if __name__ == "__main__":
    print(validate_board(board))
