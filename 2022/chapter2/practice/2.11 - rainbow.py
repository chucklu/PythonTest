from turtle import *
import numpy as np

# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)


def setRandomFillColor():
    color = tuple(np.random.randint(0, 256, 3))
    # print(color)
    fillcolor(color)
    return color


def drawCircle(r):
    up()
    home()
    global step
    global count
    setpos(pos()+(-step*count, 0))
    print(pos())
    down()
    setheading(90)

    setRandomFillColor()
    begin_fill()
    circle(r, 180)
    end_fill()


radius = 200
count = 0
step = 20

while count < 7:
    drawCircle(radius)
    radius = radius-step
    count = count+1
done()
