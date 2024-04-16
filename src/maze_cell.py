from simple_geometry import Point, Line

class Maze_Cell:
    def __init__(self, top_left_point: Point, bottom_right_point: Point, window):
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
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._window.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._window.draw_line(bottom_wall, "black")
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._window.draw_line(right_wall, "black")
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._window.draw_line(left_wall, "black")
        return