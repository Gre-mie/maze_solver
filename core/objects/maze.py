# Maze object to hold and print the cells at a see-able speed
import time
from objects.cell import Cell
from objects.point import Point

class Maze:
    def __init__(
            self, 
            win,  
            origin:Point, 
            *, 
            num_rows:int=9, 
            num_cols:int=9, 
            cell_size_x:int=47, # size 50 - line width (3)
            cell_size_y:int=47  # size 50 - line width (3)
        ):

        self.__origin = origin

        self.rows = num_rows
        self.cols = num_cols
        self.cell_x = cell_size_x
        self.cell_y = cell_size_y

        self.__win = win

        self._cells = []

        self._create_cells()


    # return an array of Cell objects, each sub array represents a column
    def _create_cells(self):

        for _ in range(self.cols):
            col = []
            for _ in range(self.rows):
                col.append(Cell(self.__win, Point(None,None), Point(None, None)))
            self._cells.append(col)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i,j)
                
    def _draw_cell(self, i, j):
        pos_x = (self.cell_x * i) + self.__origin.x
        pos_y = (self.cell_y * j) + self.__origin.y
        self._cells[i][j].draw(
                Point(pos_x, pos_y), 
                Point(pos_x + self.cell_x, pos_y + self.cell_y)
        )



    # temp method
    def debug_formatted_arguments(self):
        return [
            "Class Maze:",
            f"origin: {self.__origin}",
            f"rows: {self.rows}",
            f"cols: {self.cols}",
            f"cell x: {self.cell_x}",
            f"cell y: {self.cell_y}",
            f"cells: {self.cells}",
            f"win: {self.__win}",
        ]

    
    def __repr__(self):
        return f"Class: Maze(self, win={self.__win}, cords={self.__origin}, num_rows={self.rows}, num_cols={self.cols}, cell_size_x={self.cell_x}, cell_size_y={self.cell_y})"