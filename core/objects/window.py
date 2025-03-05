# window.py, a window object
from tkinter import Tk, BOTH, Canvas
from objects.line import Line

class Window:
    def __init__(self, width:int, height:int):

        self.__root = Tk()
        self.__root.title("Maze solver")
        
        self.width = width
        self.height = height
    
        self.canvas = Canvas(self.__root, width=self.width, height=self.height, background="#5050AA")
        self.canvas.pack()
        self.running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, col):
        line.draw(self.canvas, col)



        

    def __repr__(self):
        return f"Window(width={self.width}, height={self.height})"
