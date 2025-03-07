# Maze object to hold and print the cells at a see-able speed
import time
import random
from objects.cell import Cell
from objects.point import Point

class Maze:
    def __init__(
            self,   
            win=None,
            origin:Point=Point(0,0), 
            num_rows:int=9, 
            num_cols:int=9, 
            cell_size_x:int=47, # size 50 - line width (3)
            cell_size_y:int=47,  # size 50 - line width (3)
            speed:int= 0.05,
            background = "#FFFFFF",
            seed:int|None = None,
        ):

        self._origin = origin
        self._speed = speed
        self._background = background
        self._seed = seed
        self._win = win

        self.rows = num_rows
        self.cols = num_cols
        self.cell_x = cell_size_x
        self.cell_y = cell_size_y

        self._cells = []

        random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0) # starts at the first block in the grid
        self._reset_cells_visited()


    # return an array of Cell objects, each sub array represents a column
    # Calls draw_cell on each cell
    def _create_cells(self):
        if self.cols <= 0 or self.rows <= 0:
            raise ValueError("Rows and columns must be a positive int")

        for i in range(self.cols):
            col = []
            for j in range(self.rows):
                col.append(Cell(self._win, background=self._background))
            self._cells.append(col)

        for i in range(self.cols):
            for j in range(self.rows):
                self._draw_cell(i, j)
                

    # Set the position of a cell in the maze
    # calls .draw method on the cell
    def _draw_cell(self, i, j):
        pos_x = self._cells[i][j].p1.x
        pos_y = self._cells[i][j].p1.y

        # Does not recalculate if the position is already set
        if (
                not pos_x or
                not pos_y
            ):
            pos_x = (self.cell_x * i) + self._origin.x
            pos_y = (self.cell_y * j) + self._origin.y

            self._cells[i][j].p1 = Point(pos_x, pos_y)
            self._cells[i][j].p2 = Point(pos_x + self.cell_x, pos_y + self.cell_y)

        if self._win:
            self._cells[i][j].draw(
                    Point(pos_x, pos_y), 
                    Point(pos_x + self.cell_x, pos_y + self.cell_y)
            )
            self._animate()


    # Slows down the programme to make it look animated
    def _animate(self):
        self._win.redraw()
        time.sleep(self._speed)


    # Removes edge from top left corner and bottom right corner cells
    def _break_entrance_and_exit(self):
        self._cells[0][0].top = False
        self._draw_cell(0,0)

        self._cells[self.cols - 1][self.rows - 1].bottom = False
        self._draw_cell(self.cols - 1, self.rows - 1)


    # Walks through the maze removing walls on its way
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            # adds a direction to to_visit if its within the grid and has not been visited yet
            directions = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)] # up, down, left, right
            for direction in directions:
                a, b = direction
                if a >= 0 and b >= 0 and a < self.cols and b < self.rows:
                    if self._cells[a][b].visited == False:
                        to_visit.append((a, b))
            
            # Breaks out of the loop if there are no places to visit
            if len(to_visit) < 1:
                self._draw_cell(i, j)
                break

            # picks a random direction and removes the walls
            visit = to_visit[random.randrange(len(to_visit))]
            # up
            if visit == directions[0]:
                self._cells[i][j].top = False
                self._cells[visit[0]][visit[1]].bottom = False

            # down
            elif visit == directions[1]:
                self._cells[i][j].bottom = False
                self._cells[visit[0]][visit[1]].top = False

            # left
            elif visit == directions[2]:
                self._cells[i][j].left = False
                self._cells[visit[0]][visit[1]].right = False

            # right
            elif visit == directions[3]:
                self._cells[i][j].right = False
                self._cells[visit[0]][visit[1]].left = False

            # recurse using the cell visit
            self._break_walls_r(visit[0], visit[1])
    
    # resets the visited variable back to false
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    
    def __repr__(self):
        return f"Class: Maze(self, win={self._win}, origin={self._origin}, num_rows={self.rows}, num_cols={self.cols}, cell_size_x={self.cell_x}, cell_size_y={self.cell_y}, speed={self._speed}, background={self._background}, seed={self._seed})"