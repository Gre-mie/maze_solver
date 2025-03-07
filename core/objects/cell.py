# a cell in the maze
from objects.window import Window
from objects.line import Line
from objects.point import Point

class Cell:
    def __init__(self, window:Window=None, p1:Point=Point(None, None), p2:Point=Point(None, None), *, col="#223300", background="#FFFFFF"):
        self._win = window

        self.p1 = p1
        self.p2 = p2

        self.left = True
        self.right = True
        self.top = True
        self.bottom = True

        self._line_col = col
        self._background = background


    # Returns the center of the cell object
    def get_center(self):
 
        return Point(
            self.p1.x + (self.p2.x - self.p1.x) / 2,
            self.p1.y + (self.p2.y - self.p1.y) / 2
        )
    
    
    # Sets the position of the cells and calls draw
    # Lines are the background colour if None
    def draw(self, p1:Point, p2:Point):

        self.p1 = p1
        self.p2 = p2

        left_line = Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y))
        if self.left:
            self._win.draw_line(left_line, self._line_col)
        else:
            self._win.draw_line(left_line, self._background)
        
        right_line = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y))
        if self.right:
            self._win.draw_line(right_line, self._line_col)
        else:
            self._win.draw_line(right_line, self._line_col)

        top_line = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
        if self.top:
            self._win.draw_line(top_line, self._line_col)
        else:
            self._win.draw_line(top_line, self._background)

        bottom_line = Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y))
        if self.bottom:
            self._win.draw_line(bottom_line, self._line_col)
        else:
            self._win.draw_line(bottom_line, self._background)
    

    # draws a line from the center of This Cell to the center of the to_cell Cell
    def draw_move(self, to_cell, *, redo=False):
        line_col = "#CC2288"
        if redo:
            line_col = "grey"
        
        self._win.draw_line(Line(self.get_center(), to_cell.get_center()), line_col)

    


    def __repr__(self):
        return f"Class: Cell(self, window={self.__win}, p1={self.p1}, p2={self.p2}, col={self._line_col}, background={self._background})"
        