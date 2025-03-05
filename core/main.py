# main.py, runs the programme

from objects.window import Window
from objects.point import Point
from objects.cell import Cell


def main():
    
    window = Window(800, 600)


    # vvv temp code block vvv

    # determins the size of the cells and how many rows columns to create
    cells = []
    num_cells = 10
    size_x = window.width // num_cells
    size_y = window.height // num_cells

    # creates the cells
    for j in range(0, window.height, size_y):
        for i in range(0, window.width, size_x):
            cells.append(Cell(
                window,
                Point(i, j),
                Point(i + size_x, j + size_y)
            ))

    # prints all cells in list
    for cell in cells:
        cell.draw()

    # ^^^ temp code block ^^^




    window.wait_for_close()


if __name__ == "__main__":
    main()