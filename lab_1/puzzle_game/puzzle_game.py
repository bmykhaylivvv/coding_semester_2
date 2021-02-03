test_board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]

# Зробити перевірку, що це саме все числа, це можна зробити, коли рядок і стовпчик склеяли в один

def remove_stars(char):
    if char != '*' and char != ' ':
        return True
    else:
        return False

def numeric_chech():
    pass


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
    new_lines = []
    for line in lst:
        new_line = list(filter(remove_stars, line))
        new_lines.append(new_line)

    for ln in new_lines:
        if len(ln) != len(set(ln)):
            return False
    return True



def one_color(board):
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

print(one_color(test_board))

print(repeat_check(one_color(test_board)))

    







