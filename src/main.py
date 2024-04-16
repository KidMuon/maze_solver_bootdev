from window import Window
from simple_geometry import Point, Line
from maze_cell import Maze_Cell
from itertools import product

def main():
    win = Window(800, 600)
    
    top_left_points = []
    for x in range(4):
        for y in range(4):
            top_left_points.append(Point(x * 125 + 50, y * 125 + 50))
    
    bottom_right_points = [Point(list_point.x + 110, list_point.y + 110) for list_point in top_left_points]

    maze_cell_origins = zip(top_left_points, bottom_right_points)

    maze_cells = []
    for top_left, bottom_right in maze_cell_origins:
        maze_cells.append(Maze_Cell(top_left, bottom_right, win))

    wall_filters = list(product([True, False], repeat=4))
    for i in range(16):
        maze_cells[i].has_left_wall = wall_filters[i][0]
        maze_cells[i].has_right_wall = wall_filters[i][1]
        maze_cells[i].has_top_wall = wall_filters[i][2]
        maze_cells[i].has_bottom_wall = wall_filters[i][3]
    
    for maze_cell in maze_cells:
        print(maze_cell)
        maze_cell.draw()
    
    win.wait_for_close()


if __name__ == '__main__':
    main()
