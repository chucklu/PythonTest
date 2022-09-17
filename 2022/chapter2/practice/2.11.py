from turtle import *
import numpy as np

# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)

def setRandomFillColor():
    color = tuple(np.random.randint(0, 256, 3))
    print(color)
    fillcolor(color)
    return color

def drawCircle(r):
    up()
    home()
    setpos(pos()+(0, -r))
    down()

    setRandomFillColor()
    begin_fill()
    circle(r)
    end_fill()

radius = 200
count = 9
step = 20

while count > 0:
    drawCircle(radius)
    radius = radius-step
    count = count-1
done()
