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
for angle in [0,120,120]:
    right(angle)
    drawKoch(300,3)
done()
