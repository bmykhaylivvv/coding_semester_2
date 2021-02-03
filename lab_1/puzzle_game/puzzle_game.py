test_board = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3   5  **",
    "  1  2***",
    "  7  ****"
]

# Зробити перевірку, що це саме все числа, це можна зробити, коли рядок і стовпчик склеяли в один


def remove_stars(char):
    if char != '*' and char != ' ':
        return True
    else:
        return False


def numeric_check(colors):
    """
    Doc
    """
    numbers_plus_blank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    for color in colors:
        for char in color:
            if char not in numbers_plus_blank:
                return False
    return True


def horizontal_lines(board):
    """
    Doc
    """
    horizontals = []
    for line in board:
        line_list = list(line)
        horizontals.append(line_list)
    return horizontals


def vertical_lines(board):
    """
    Doc
    """
    verticals = []
    column = []
    for position in range(len(board)):
        for row in board:
            column.append(row[position])
        verticals.append(column)
        column = []
    return verticals


def repeat_check(lst):
    """
    Doc
    """
    new_lines = []
    for line in lst:
        new_line = list(filter(remove_stars, line))
        new_lines.append(new_line)

    for ln in new_lines:
        if len(ln) != len(set(ln)):
            return False
    return True


def one_color(board):
    """
    Doc
    """
    same_color = []
    vertical = []
    for i in range(5):
        vertical.append(vertical_lines(board)[i][(4 - i):(9 - i)])

    horizontal = []
    for j in range(5):
        horizontal.append(horizontal_lines(test_board)[8 - j][(1 + j):(5 + j)])

    for k in range(len(vertical)):
        same_color.append(vertical[k] + horizontal[k])

    return same_color


def validate_board(board):
    """
    Doc
    """
    if repeat_check(horizontal_lines(board)) and repeat_check(vertical_lines(board))\
            and repeat_check(one_color(board)) and numeric_check(one_color(board)):
        return True
    return False


print(validate_board(test_board))
