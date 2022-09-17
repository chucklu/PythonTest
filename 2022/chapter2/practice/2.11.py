from turtle import *

def drawCircle(r):
    up()
    home()
    setpos(pos()+(0, -r))
    down()
    circle(r)

radius = 200
count = 9
step = 20

while count > 0:
    drawCircle(radius)
    radius = radius-step
    count = count-1
done()
