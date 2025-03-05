# main.py, runs the programme

from objects.window import Window
from objects.point import Point
# from objects.cell import Cell
from objects.maze import Maze


def main():
    
    window = Window(800, 600)

    maze = Maze(window, Point(10, 10))
    
    print(maze, "\n")
    for v in maze.debug_formatted_arguments():
        print(v)


    # vvv temp code block vvv

    # determins the size of the cells and how many rows columns to create
#    cells = []
 #   num_cells = 9
  #  size_x = window.width // num_cells
   # size_y = window.height // num_cells

    # creates the cells

#    for j in range(0, window.height, size_y):
 #       if len(cells) > num_cells - 1:
  #          break
   #     row = []
    #    for i in range(0, window.width, size_x):
     #       if len(row) > num_cells -1:
      #          break
       #     row.append(Cell(
        #        window,
         #       Point(i, j),
          #      Point(i + size_x, j + size_y)
           # ))
#        cells.append(row)

    # prints all cells in list
 #   for row in cells:
  #      for cell in row:
   #         cell.draw()

    # testing drawing path function
#    cells[3][3].draw_move(cells[3][4])
 #   cells[3][4].draw_move(cells[3][5])
  #  cells[3][5].draw_move(cells[4][5], redo=True)
   # cells[4][5].draw_move(cells[5][5], redo=True)
    #cells[5][5].draw_move(cells[5][4])
#    cells[5][4].draw_move(cells[5][3])
 #   cells[5][3].draw_move(cells[4][3], redo=True)
  #  cells[4][3].draw_move(cells[3][3], redo=True)


#    print(f"cells:\ncols: {len(cells[1])}\nrows: {len(cells)}")

    # ^^^ temp code block ^^^




    window.wait_for_close()


if __name__ == "__main__":
    main()