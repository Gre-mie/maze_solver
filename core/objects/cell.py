# a cell in the maze
from objects.window import Window
from objects.line import Line
from objects.point import Point

class Cell:
    def __init__(self, window:Window, p1:Point, p2:Point):
        self.__win = window

        self.p1 = p1
        self.p2 = p2

        self.left = Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y))
        self.right = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y))
        self.top = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
        self.bottom = Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y))
    
    def draw(self):
        if self.left:
            self.__win.draw_line(self.left, "black")
        if self.right:
            self.__win.draw_line(self.right, "black")
        if self.top:
            self.__win.draw_line(self.top, "red")
        if self.bottom:
            self.__win.draw_line(self.bottom, "red")



    def __repr__(self):
        return f"Class: Cell(self, window={self.__win}, p1={self.p1}, p2={self.p2}):"
        