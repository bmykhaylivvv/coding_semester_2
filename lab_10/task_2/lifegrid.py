'''
Module for LifeGrid class.
'''
from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                self._grid[row, col] = 'D'

        for pos in coord_list:
            self._grid[pos[0], pos[1]] = 'L'

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        if self._grid[row, col] == 'L':
            return True

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = 'D'

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = 'L'

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        live_neighbors = 0
        try:
            if self._grid[row-1, col] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        try:
            if self._grid[row+1, col] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        try:
            if self._grid[row, col-1] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        try:
            if self._grid[row, col+1] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        try:
            if self._grid[row-1, col-1] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        try:
            if self._grid[row-1, col+1] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        try:
            if self._grid[row+1, col-1] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        try:
            if self._grid[row+1, col+1] == 'L':
                live_neighbors += 1
        except AssertionError:
            pass
        return live_neighbors

    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        res = ''
        # for i in range(len(self.num_rows())):
        #     print('1')
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                res += str(self._grid[row, col])
            res += '\n'
        return res[:-1]
