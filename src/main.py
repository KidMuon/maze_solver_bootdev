from window import Window
from simple_geometry import Point, Line

def main():
    win = Window(800, 600)
    point_1 = Point(50, 50)
    point_2 = Point(600, 450)
    red_line = Line(start=point_1, end=point_2)
    win.draw_line(red_line, "red")
    win.wait_for_close()


if __name__ == '__main__':
    main()
