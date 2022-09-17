# 正N边形的绘制
from turtle import *
import numpy as np

def setRandomFillColor():
    color = tuple(np.random.randint(0, 256, 3))
    print(color)
    fillcolor(color)
    return color

def drawN(n):
    begin_fill()
    setRandomFillColor()
    temp = 180*(n-2)/n
    angle = 180 - temp
    while True:
        forward(200)
        print(angle)
        right(angle)
        #print("position:{}, heading:{}".format(pos(),heading()))
        if (abs(pos())) < 1:
            break
    end_fill()

# Creating the screen object
screen = Screen()
# Setting the screen color-mode
screen.colormode(255)

count = 9
while count > 2:
    drawN(count)
    count -= 1

done()
