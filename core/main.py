# main.py, runs the programme

from objects.window import Window
from objects.point import Point
from objects.cell import Cell


def main():
    
    window = Window(800, 600)

#    line = Line(Point(0, 0), Point(100, 100))
 #   window.draw_line(line, "black")



    # vvv temp code block vvv
    # !!! No longer works due to no relevent imports !!!
#    # practice drawing lines
 #   print(f"window: width: {window.width}  height: {window.height}")
  #  padding = 1.5
   # num_of_boxes = 10
    #line_width = (window.width - padding * 2) / num_of_boxes
#    line_height = (window.height - padding * 2) / num_of_boxes
 #   w = padding
  #  h = padding
   # last_w = w + line_width
    #last_h = h + line_height
#    while h <= window.height:
 #       while w <= window.width:
  #          line1 = Line(Point(last_w, h), Point(w, h))
   #         line2 = Line(Point(w, last_h), Point(w, h))
    #        print(f"L1:  p1: x: {line1.p1.x}  y: {line1.p1.y}  p2: x: {line1.p2.x}  y: {line1.p2.y}")
     #       print(f"L1:  p1: x: {line2.p1.x}  y: {line2.p1.y}  p2: x: {line2.p2.x}  y: {line2.p2.y}")
      #      window.draw_line(line1, "black")
       #     window.draw_line(line2, "red")

#            last_w = w
 #           w += line_width
        
#        last_w = padding
 #       w = last_w

  #      h += line_height
    # ^^^ temp code block ^^^

    cell_size = 100
    half_cell = cell_size / 2
    center_x = window.width / 2
    center_y = window.height / 2
    cell1 = Cell(window, Point(
            center_x - half_cell,
            center_y - half_cell
        ), Point(
            center_x + half_cell,
            center_y + half_cell
        ))
    cell1.draw()


    window.wait_for_close()


if __name__ == "__main__":
    main()