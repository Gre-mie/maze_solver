# main.py, runs the programme
from objects.window import Window
from objects.point import Point
# from objects.cell import Cell
from objects.maze import Maze


def main():

    window_width = 800
    window_height = 600
    background_col = "#5050AA"
    
    window = Window(window_width, window_height, background_col)

    cell_width = 50
    cell_height = 50

    maze = Maze(
            window,
            Point(cell_width, cell_height), # size of the cell used for padding also 
            num_rows = window_height // cell_width - 2, # how many rows there are in the maze
            num_cols = window_width // cell_height - 2, # how many cells in a row
            cell_size_x = cell_width,
            cell_size_y = cell_height,
            speed = 0.005,
            background = background_col,
            #seed=0,
        )





    window.wait_for_close()


if __name__ == "__main__":
    main()