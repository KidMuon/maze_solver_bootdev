from window import Window
from simple_geometry import Point, Line
from maze_cell import Maze_Cell
from itertools import product

def main():
    win = Window(800, 600)

    c1 = Maze_Cell(Point(50, 50), Point(100, 100), win)
    c1.has_right_wall = False
    c1.draw()

    c2 = Maze_Cell(Point(100, 50), Point(150, 100), win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw()

    c1.draw_move(c2)

    c3 = Maze_Cell(Point(100, 100), Point(150, 150), win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw()

    c2.draw_move(c3)

    c4 = Maze_Cell(Point(150, 100), Point(200, 150), win)
    c4.has_left_wall = False
    c4.draw()

    c3.draw_move(c4, True)

    win.wait_for_close()


if __name__ == '__main__':
    main()
