import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_entrance_and_exit_open(self):
        m1 = Maze(0, 0, 2, 2, 10, 10)
        m1._create_cells()
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_cell_visited_flags(self):
        rows, cols = 20, 20
        m1 = Maze(100, 100, rows, cols, 25, 25)
        m1._create_cells()
        for col_index in range(cols):
            for row_index in range(rows):
                self.assertFalse(m1._cells[col_index][row_index].visited)
        m1._break_all_the_walls()
        for col_index in range(cols):
            for row_index in range(rows):
                self.assertTrue(m1._cells[col_index][row_index].visited)
        m1._reset_cells_visited()
        for col_index in range(cols):
            for row_index in range(rows):
                self.assertFalse(m1._cells[col_index][row_index].visited)

    def test_cells_connected_function(self):
        m1 = Maze(10, 10, 1, 3, 3, 3)
        m1.generate()
        self.assertTrue(m1._cells_connected(0, 0, 1, 0))
        self.assertTrue(m1._cells_connected(1, 0, 2, 0))
        self.assertFalse(m1._cells_connected(0, 0, 2, 0))
        self.assertTrue(m1._cells_connected(1, 0, 0, 0))
        self.assertTrue(m1._cells_connected(2, 0, 1, 0))
        self.assertFalse(m1._cells_connected(2, 0, 0, 0))

        m2 = Maze(10, 10, 3, 1, 3, 3)
        m2.generate()
        self.assertTrue(m2._cells_connected(0, 0, 0, 1))
        self.assertTrue(m2._cells_connected(0, 1, 0, 2))
        self.assertFalse(m2._cells_connected(0, 0, 0, 2))
        self.assertTrue(m2._cells_connected(0, 1, 0, 0))
        self.assertTrue(m2._cells_connected(0, 2, 0, 1))
        self.assertFalse(m2._cells_connected(0, 2, 0, 0))


if __name__ == "__main__":
    unittest.main()