from maze_cell import Maze_Cell
from simple_geometry import Point
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = win
        self._cells = []

    def _create_cells(self):
        for col_index in range(self.num_cols):
            self._cells.append([])
            for row_index in range(self.num_rows):
                cell_start_x = self.cell_size_x * col_index + self.x1
                cell_end_x = cell_start_x + self.cell_size_x
                cell_start_y = self.cell_size_y * row_index + self.y1
                cell_end_y = cell_start_y + self.cell_size_y
                
                new_cell = Maze_Cell(Point(cell_start_x, cell_start_y), Point(cell_end_x, cell_end_y), self.window)

                self._cells[col_index].append(new_cell)

        for col_index in range(self.num_cols):
            for row_index in range(self.num_rows):
                self._draw_cell(col_index, row_index)        


    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)