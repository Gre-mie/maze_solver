# window.py, a window object
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self):

        self.root = Tk()
        self.root.title("Maze solver")
        

        self.canvas = Canvas(self.root, background="#5050AA").pack()


    
    def run(self): # temp code for testing only
        self.root.mainloop()

        

    def __repr__(self):
        return f"Window(width={self.width}, height={self.height})"
