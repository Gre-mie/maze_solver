# a cell in the maze
from objects.window import Window
from objects.line import Line
from objects.point import Point

class Cell:
    def __init__(self, window:Window, p1:Point, p2:Point, *, col="#223300"):
        self.__win = window

        self.p1 = p1
        self.p2 = p2

        self.left = True
        self.right = True
        self.top = True
        self.bottom = True

        self.line_col = col


    # Returns the center of the cell object
    def get_center(self):
 
        return Point(
            self.p1.x + (self.p2.x - self.p1.x) / 2,
            self.p1.y + (self.p2.y - self.p1.y) / 2
        )
    
    
    # Sets the position of the cells and calls draw
    def draw(self, p1:Point, p2:Point):

        self.p1 = p1
        self.p2 = p2

        if self.left:
            left_line = Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y))
            self.__win.draw_line(left_line, self.line_col)
        if self.right:
            right_line = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y))
            self.__win.draw_line(right_line, self.line_col)
        if self.top:
            top_line = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
            self.__win.draw_line(top_line, self.line_col)
        if self.bottom:
            bottom_line = Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y))
            self.__win.draw_line(bottom_line, self.line_col)
    

    # draws a line from the center of This Cell to the center of the to_cell Cell
    def draw_move(self, to_cell, *, redo=False):
        line_col = "#CC2288"
        if redo:
            line_col = "grey"
        
        self.__win.draw_line(Line(self.get_center(), to_cell.get_center()), line_col) # use the helper funciton here


    def __repr__(self):
        return f"Class: Cell(self, window={self.__win}, p1={self.p1}, p2={self.p2}):"
        