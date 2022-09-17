# 正N边形的绘制
from turtle import *
import numpy as np


def initPos():
    up()
    home()
    setpos(pos()+(-180, 400))
    down()


def setRandomFillColor():
    color = tuple(np.random.randint(0, 256, 3))
    print(color)
    fillcolor(color)
    return color


def drawN(n):
    begin_fill()
    initPos()
    setRandomFillColor()
    tempAngle = 180*(n-2)/n
    angle = 180 - tempAngle
    print(angle)
    tempCount = n
    while True:
        tempCount -= 1
        forward(160)
        right(angle)
        #print("position:{}, heading:{}".format(pos(),heading()))
        if (tempCount <= 0):
            break
    end_fill()


# Creating the screen object
screen = Screen()
# Setting the screen color-mode
screen.colormode(255)

count = 16
while count > 2:
    drawN(count)
    count -= 1

done()
