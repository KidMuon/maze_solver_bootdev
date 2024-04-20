from simple_geometry import Point, Line

WALL_PRESENT_COLOR = "black"
WALL_ABSENT_COLOR = "#d9d9d9"

class Maze_Cell:
    def __init__(self, top_left_point: Point, bottom_right_point: Point, window = None):
        self._x1 = top_left_point.x
        self._y1 = top_left_point.y
        self._x2 = bottom_right_point.x
        self._y2 = bottom_right_point.y
        self._window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))

        top_wall_color = WALL_PRESENT_COLOR if self.has_top_wall else WALL_ABSENT_COLOR
        bottom_wall_color = WALL_PRESENT_COLOR if self.has_bottom_wall else WALL_ABSENT_COLOR
        right_wall_color = WALL_PRESENT_COLOR if self.has_right_wall else WALL_ABSENT_COLOR
        left_wall_color = WALL_PRESENT_COLOR if self.has_left_wall else WALL_ABSENT_COLOR

        self._window.draw_line(top_wall, top_wall_color)
        self._window.draw_line(bottom_wall, bottom_wall_color)
        self._window.draw_line(right_wall, right_wall_color)
        self._window.draw_line(left_wall, left_wall_color)
        
        return

    def __repr__(self):
        return f"Maze_Cell x1: {self._x1}, y1: {self._y1}, x2: {self._x2}, y2: {self._y2}" + '\n' + f"walls: {self.has_top_wall},{self.has_bottom_wall},{self.has_left_wall},{self.has_right_wall}"

    def get_center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False):
        start = self.get_center()
        end = to_cell.get_center()
        connecting_line = Line(start, end)
        if undo:
            self._window.draw_line(connecting_line, "gray")
        else:
            self._window.draw_line(connecting_line, "red")