# main.py, runs the programme
from objects.window import Window
from objects.point import Point
from objects.maze import Maze


def main():

    window_width = 800
    window_height = 600
    
    window = Window(window_width, window_height)

    cell_width = 50
    cell_height = 50
    maze = Maze(
            window,
            Point(cell_width, cell_height), # size of the cell used for padding also 
            num_rows = window_height // cell_width - 2, # how many rows there are in the maze
            num_cols = window_width // cell_height - 2, # how many cells in a row
            cell_size_x = cell_width,
            cell_size_y = cell_height
        )

    window.wait_for_close()


if __name__ == "__main__":
    main()