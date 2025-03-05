# a cell in the maze
from objects.window import Window
from objects.line import Line
from objects.point import Point

class Cell:
    def __init__(self, window:Window, p1:Point, p2:Point):
        self.__win = window

        self.p1 = p1
        self.p2 = p2
        self.center = (Point(
                self.p1.x + (self.p2.x - self.p1.x) / 2, 
                self.p1.y + (self.p2.y - self.p1.y) / 2
            ))

        # these should be set to boolan values
        self.left = Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y))
        self.right = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y))
        self.top = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
        self.bottom = Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y))

        self.line_col = "#223300"

    
    # Possibly needs reworking
    def draw(self):
        if self.left:
            self.__win.draw_line(self.left, self.line_col)
        if self.right:
            self.__win.draw_line(self.right, self.line_col)
        if self.top:
            self.__win.draw_line(self.top, self.line_col)
        if self.bottom:
            self.__win.draw_line(self.bottom, self.line_col)
    
    # draws a line from the center of This Cell to the center of the to_cell Cell
    def draw_move(self, to_cell, *, redo=False):
        line_col = "#CC2288"
        if redo:
            line_col = "grey"
        
        self.__win.draw_line(Line(self.center, to_cell.center), line_col)



    def __repr__(self):
        return f"Class: Cell(self, window={self.__win}, p1={self.p1}, p2={self.p2}):"
        