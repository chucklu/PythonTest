from turtle import *


def drawKoch(length, level):
    tempLength = length/3.0
    if(level==0):
        forward(length)
        return
    else:
        drawKoch(tempLength,level-1)
        left(60)
        drawKoch(tempLength,level-1)
        right(120)
        drawKoch(tempLength,level-1)
        left(60)
        drawKoch(tempLength,level-1)

speed(0)
drawKoch(600,3)
done()
