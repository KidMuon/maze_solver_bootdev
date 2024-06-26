from window import Window
from simple_geometry import Point, Line
from maze_cell import Maze_Cell
from itertools import product
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 20, 28, 25, 25, win)
    #maze = Maze(50, 50, 1, 2, 200, 200, win)
    maze.generate()
    maze.solve()
    print("Solve Returned")
    win.wait_for_close()


if __name__ == '__main__':
    main()
