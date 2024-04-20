from maze_cell import Maze_Cell
from simple_geometry import Point
import time, random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = win

        if seed is not None:
            self.seed = random.seed(seed)

        self._cells = []

        self._create_cells()
        self._break_all_the_walls()

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
        
        self._draw_maze()
    
    def _draw_maze(self):
        if not self.window:
            return 

        for col_index in range(self.num_cols):
            for row_index in range(self.num_rows):
                self._draw_cell(col_index, row_index)        

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        # time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_maze()

    def _break_all_the_walls(self):
        self._break_entrance_and_exit()

        start_row = self.num_rows // 2
        start_col = self.num_cols // 2

        self._break_walls_r(start_col, start_row)
        self._draw_maze()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            visitable_neighbors = []

            # Check if the neighbor above has been visited
            if 0 <= i - 1 < self.num_cols and not self._cells[i - 1][j].visited:
                visitable_neighbors.append((i - 1, j))

            # Check if the neighbor below has been visited
            if 0 <= i + 1 < self.num_cols and not self._cells[i + 1][j].visited:
                visitable_neighbors.append((i + 1, j))
            
            # Check if the neighbor to the left has been visited
            if 0 <= j - 1 < self.num_rows and not self._cells[i][j - 1].visited:
                visitable_neighbors.append((i, j - 1))

            # Check if the neighbor to the right has been visited
            if 0 <= j + 1 < self.num_rows and not self._cells[i][j + 1].visited:
                visitable_neighbors.append((i, j + 1))

            if len(visitable_neighbors) == 0:
                break
            
            i_, j_ = visitable_neighbors[random.randrange(len(visitable_neighbors))]
            
            self._break_between(i, j, i_, j_)
            self._break_walls_r(i_, j_)

    def _break_between(self, i, j, i_, j_):
        if j > j_:
            self._cells[i][j].has_top_wall = False
            self._cells[i_][j_].has_bottom_wall = False
        if j < j_:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i_][j_].has_top_wall = False
        if i > i_:
            self._cells[i][j].has_left_wall = False
            self._cells[i_][j_].has_right_wall = False
        if i < i_:
            self._cells[i][j].has_right_wall = False
            self._cells[i_][j_].has_left_wall = False
        
    def _reset_cells_visited(self):
        for col_index in range(self.num_cols):
            for row_index in range(self.num_rows):
                self._cells[col_index][row_index].visited = False