from window import Window
from simple_geometry import Point, Line
from maze_cell import Maze_Cell
from itertools import product
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(100, 100, 20, 20, 25, 25, win)
    maze._create_cells()
    maze._break_entrance_and_exit()

    win.wait_for_close()


if __name__ == '__main__':
    main()
