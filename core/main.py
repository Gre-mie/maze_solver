# main.py, runs the programme

from objects.window import Window
from objects.line import Line
from objects.point import Point

def main():
    
    window = Window(800, 600)

    line = Line(Point(0, 0), Point(100, 100))
    line.draw(window.canvas, "red")




    window.wait_for_close()


if __name__ == "__main__":
    main()