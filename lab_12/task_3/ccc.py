    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        cur_pos = _CellPosition(self._start_cell.row, self._start_cell.col)
        ways = ((-1, 0), (0, 1), (1, 0), (0, -1))
        print(self._exit_cell.row, self._exit_cell.col)
        while cur_pos.row != self._exit_cell.row and cur_pos.col != self._exit_cell.col:
            print(cur_pos)
            for move_row, move_col in ways:
                new_pos = _CellPosition(cur_pos.row + move_row, cur_pos.col + move_col)
                if self._valid_move(new_pos.row, new_pos.col):
                    print(new_pos.row, new_pos.col)
            #         print('hi')
                    self._maze_cells[cur_pos.row, cur_pos.col] = self.PATH_TOKEN
                    cur_pos = _CellPosition(new_pos.row, new_pos.col)
                    pass



# ІІ
    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        cur_pos = _CellPosition(self._start_cell.row, self._start_cell.col)
        new_pos = cur_pos
        ways = ((-1, 0), (0, 1), (1, 0), (0, -1))
        while True:
            print(f'EXIT: {self._exit_cell}, CURRENT: {cur_pos}')
            if cur_pos != _CellPosition(self._exit_cell.row, self._exit_cell.col):
                # print(new_pos)
                for way_row, way_col in ways:
                    new_pos = _CellPosition(cur_pos.row+way_row, cur_pos.col+way_col)
                    print(cur_pos)
                    # self._maze_cells[cur_pos.row, cur_pos.col] = self.TRIED_TOKEN
                    if self._valid_move(new_pos.row, new_pos.col):
                        # print(new_pos)
                        self._maze_cells[cur_pos.row, cur_pos.col] = self.PATH_TOKEN
                        cur_pos = new_pos
                        
                    continue
            self._maze_cells[cur_pos.row, cur_pos.col] = self.PATH_TOKEN
            if self._exit_cell.row == cur_pos.row and self._exit_cell.col == cur_pos.col:
                break