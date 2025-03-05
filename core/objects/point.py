# stores a single point as x and y
class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Class: Point(self, x={self.x}, y={self.y})"
