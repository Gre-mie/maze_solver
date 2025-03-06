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
            cell_size_y:int=47,  # size 50 - line width (3)
            speed:int= 0.05
        ):

        self._origin = origin

        self.rows = num_rows
        self.cols = num_cols
        self.cell_x = cell_size_x
        self.cell_y = cell_size_y

        self._speed = speed
        self._win = win

        self._cells = []

        self._create_cells()


    # return an array of Cell objects, each sub array represents a column
    # Calls draw_cell on each cell
    def _create_cells(self):

        for _ in range(self.cols):
            col = []
            for _ in range(self.rows):
                col.append(Cell(self._win, Point(None,None), Point(None, None)))
            self._cells.append(col)

        for i in range(self.cols):
            for j in range(self.rows):
                self._draw_cell(i, j)
                

    # Set the position of a cell in the maze
    # calls .draw method on the cell
    def _draw_cell(self, i, j):
        pos_x = (self.cell_x * i) + self._origin.x
        pos_y = (self.cell_y * j) + self._origin.y
        self._cells[i][j].draw(
                Point(pos_x, pos_y), 
                Point(pos_x + self.cell_x, pos_y + self.cell_y)
        )

        self._animate()


    # Slows down the programme to make it look animated
    def _animate(self):
        self._win.redraw()
        time.sleep(self._speed)

    
    def __repr__(self):
        return f"Class: Maze(self, win={self._win}, cords={self._origin}, num_rows={self.rows}, num_cols={self.cols}, cell_size_x={self.cell_x}, cell_size_y={self.cell_y})"