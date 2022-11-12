from turtle import *


def drawKoch(length, level):
    tempLength = length/3.0
    if(level==0):
        forward(length)
        return
    elif(level==1):
        forward(tempLength)
        left(60)
        forward(tempLength)
        right(120)
        forward(tempLength)
        left(60)
        forward(tempLength)
    else:
        drawKoch(tempLength,level-1)
        left(60)
        drawKoch(tempLength,level-1)
        right(120)
        drawKoch(tempLength,level-1)
        left(60)
        drawKoch(tempLength,level-1)

speed(0)
drawKoch(300,3)
done()
