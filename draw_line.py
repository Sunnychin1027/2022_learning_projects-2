"""
File: draw_line.py
Name: Sunny
-------------------------
This program let users to draw straight lines.
For the first(odd) click, user will get a hollow circle,
then, the second(even) click, user will get a black line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 30
window = GWindow()

count = 0
circle_x = 0
circle_y = 0
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    """
    This function will help us create line. On the first mouse click(odd click),
     we will get a hollow circle, which will be th line start spot, and ending
     with the next mouse click(even click).
    """
    global count, circle, circle_x, circle_y
    count += 1
    if count % 2 == 1:
        circle_x = event.x - SIZE/2
        circle_y = event.y - SIZE/2
        window.add(circle, circle_x, circle_y)
    else:
        # Get the previous circle position from global, and make a line to the second point
        line = GLine(circle_x + SIZE/2, circle_y + SIZE/2, event.x, event.y)
        window.add(line)
        window.remove(circle)


if __name__ == "__main__":
    main()
