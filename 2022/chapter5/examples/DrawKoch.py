from turtle import *


def drawKoch(length, level):
    tempLength = length/3.0
    if (level == 0):
        forward(length)
        return
    else:
        for angle in [0, 60, -120, 60]:
            left(angle)
            drawKoch(tempLength, level-1)


speed(0)
drawKoch(600, 3)
done()
