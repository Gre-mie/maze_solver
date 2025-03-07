# Unit tests
import unittest
from objects.point import Point
from objects.maze import Maze

class Tests(unittest.TestCase):

    def test_maze_row_column_creation_even(self):
        rows = 10
        cols = 12
        maze = Maze(num_rows=rows, num_cols=cols,)
        self.assertEqual(len(maze._cells), cols)
        self.assertEqual(len(maze._cells[0]), rows)
    

    def test_maze_row_column_creation_odd(self):
        cols = 3
        rows = 5
        maze = Maze(num_cols=cols, num_rows=rows,)
        self.assertEqual(len(maze._cells), cols)
        self.assertEqual(len(maze._cells[0]), rows)


    def test_maze_row_column_creation_zero_val_cols(self):
        cols = 0
        rows = 5
        with self.assertRaises(ValueError):
            maze = Maze(num_cols=cols, num_rows=rows)
    

    def test_maze_row_column_creation_zero_val_rows(self):
        cols = 5
        rows = 0
        with self.assertRaises(ValueError):
            maze = Maze(num_cols=cols, num_rows=rows)

    def test_entrance_exits_average_maze(self):
        cols = 5
        rows = 5
        maze = Maze(num_cols=cols, num_rows=rows)

        self.assertEqual(maze._cells[0][0].top, False)
        self.assertEqual(maze._cells[cols - 1][rows - 1].bottom, False)

    def test_entrance_exits_one_cell_maze(self):
        cols = 1
        rows = 1
        maze = Maze(num_cols=cols, num_rows=rows)

        self.assertEqual(maze._cells[0][0].top, False)
        self.assertEqual(maze._cells[cols - 1][rows - 1].bottom, False)
    
    def test_reset_cells_visited(self):
        cols = 5
        rows = 5
        maze = Maze(num_cols=cols, num_rows=rows)
        maze._reset_cells_visited()

        for col in maze._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)
    
        
    
    
if __name__ == "__main__":
    unittest.main()