"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
            col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
            col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
            col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        way = Stack()
        way.push(_CellPosition(self._start_cell.row, self._start_cell.col))
        while True:
            counter = 0
            try:
                cur_pos = way.peek()
            except AssertionError:
                return False
            if cur_pos.row == self._exit_cell.row and cur_pos.col == self._exit_cell.col:
                self._mark_path(cur_pos.row, cur_pos.col)
                return True
            if self._valid_move(cur_pos.row-1, cur_pos.col):
                way.push(_CellPosition(cur_pos.row-1, cur_pos.col))
                self._mark_path(cur_pos.row, cur_pos.col)
                counter += 1
                continue
            if self._valid_move(cur_pos.row, cur_pos.col+1):
                way.push(_CellPosition(cur_pos.row, cur_pos.col+1))
                self._mark_path(cur_pos.row, cur_pos.col)
                counter += 1
                continue
            if self._valid_move(cur_pos.row+1, cur_pos.col):
                way.push(_CellPosition(cur_pos.row+1, cur_pos.col))
                self._mark_path(cur_pos.row, cur_pos.col)
                counter += 1
                continue
            if self._valid_move(cur_pos.row, cur_pos.col-1):
                way.push(_CellPosition(cur_pos.row, cur_pos.col-1))
                self._mark_path(cur_pos.row, cur_pos.col)
                counter += 1
                continue

            self._mark_tried(cur_pos.row, cur_pos.col)
            way.pop()

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row in range(self._maze_cells.num_rows()):
            for col in range(self._maze_cells.num_cols()):
                if self._maze_cells[row, col] != '*':
                    self._maze_cells[row, col] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        maze = ''
        for row in range(self.num_rows()):
            line = ''
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] is None:
                    line += '_ '
                else:
                    line += f'{self._maze_cells[row, col]} '
            maze += line + '\n'

        return maze[:-1]

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
            and col >= 0 and col < self.num_cols() \
            and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f'{self.row}, {self.col}'
