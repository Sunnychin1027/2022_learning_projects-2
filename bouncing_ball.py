"""
File: bouncing_ball.py
Name: Sunny
-------------------------
This program will start since user clicked mouse,
it can bounce three round, every round will ends when the
ball bounce out of the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global variable
window = GWindow(800, 500, title='bouncing_ball.py')
d = 460
count = 0
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
moving = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global moving, count
    ball.filled = True
    window.add(ball)
    onmouseclicked(event)
    while True:
        v = 0
        if moving and count < 3:
            moving = False
            while True:
                # Set breakpoint
                if ball.x + SIZE >= window.width or count == 3:
                    count += 1
                    break
                else:
                    ball.move(VX, v)
                    v = v + GRAVITY
                    pause(DELAY)
                    if ball.y + ball.height >= window.height:
                        v = -v * REDUCE
                        pause(DELAY)
            window.remove(ball)
            window.add(ball, x=START_X, y=START_Y)
            moving = False
        pause(DELAY)


def event(bounce):
    """
    This function is the switch to determine
    the mouse click.
    """
    global count, moving
    moving = True




if __name__ == "__main__":
    main()
