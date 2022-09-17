import imp
from operator import le
from turtle import *
import numpy as np

sum = 0
step = 20
length = 10


def setRandomPenColor():
    color = tuple(np.random.randint(0, 256, 3))
    print(color)
    pencolor(color)
    return color


def drawSnake():
    global length
    global step
    length += step
    setRandomPenColor()
    circle(length, 60)

    setRandomPenColor()
    circle(length, 60)

    setRandomPenColor()
    circle(length, 60)
    #print(heading())


# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)


pensize(15)
left(90)

while True:
    drawSnake()
    sum += 1
    if (sum >= 7):
        break
done()
