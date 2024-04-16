class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2

    def draw(self, canvas, fill):
        canvas.create_line(self.start.x, self.start.y,
                           self.end.x, self.end.y,
                           fill=fill,
                           width=2)
        canvas.pack()