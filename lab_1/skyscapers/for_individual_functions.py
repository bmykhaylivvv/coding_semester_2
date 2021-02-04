def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    def horizontal_visibility(line):
        if line[0] != '*':
            pivot = int(line[0])
            counter = 1
            highest = line[1]
            for i in range(2, len(line[1:-1]) + 1):
                if line[i] > highest:
                    counter += 1
                    highest = line[i]

            if counter == pivot:
                return True
            return False
        pass

    board = board + [line[::-1] for line in board]

    tf = []
    for ln in board:
        res = horizontal_visibility(ln)
        if res is not None:
            tf.append(res)

    return all(tf)









def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    reversed_board = []
    for line in range(len(board)):
        new_line = ''
        for char in range(len(board[line])):
            new_line += board[char][line]
        reversed_board.append(new_line)

    return check_horizontal_visibility(reversed_board)



import doctest
doctest.testmod()
print(check_columns(['***21**', 
                     '412453*',
                     '423145*',
                     '*543215', 
                     '*35214*', 
                     '*41232*',
                     '*2*1***']))

board = ['***21**',\
         '412453*',\
         '423145*',\
         '*543215',\
         '*35214*',\
         '*41532*',\
         '*2*1***']

reversed_board = []
for line in range(len(board)):
    new_line = ''
    for char in range(len(board[line])):
        new_line += board[char][line]
    reversed_board.append(new_line)

# print(check_horizontal_visibility(reversed_board))