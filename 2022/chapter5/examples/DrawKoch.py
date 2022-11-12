from turtle import *


def drawKoch(length):
    tempLength = length/3.0
    forward(tempLength)
    left(60)
    forward(tempLength)
    right(120)
    forward(tempLength)
    left(60)
    forward(tempLength)


drawKoch(300)
done()
