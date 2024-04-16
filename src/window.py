from tkinter import Tk, BOTH, Canvas
from simple_geometry import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(height=height, width=width)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def set_title(self, title):
        self.__root.title = title

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window was closed...")

    def close(self):
        self.running = False

    def draw_line(self, line, fill):
        line.draw(self.__canvas, fill)
