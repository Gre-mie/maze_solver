# main.py, runs the programme

from objects.window import Window
from objects.point import Point
from objects.cell import Cell
from objects.maze import Maze


def main():
    
    window = Window(800, 600)

    maze = Maze(window, Point(50, 50))
    

    # vvv temp code block vvv



    # ^^^ temp code block ^^^




    window.wait_for_close()


if __name__ == "__main__":
    main()