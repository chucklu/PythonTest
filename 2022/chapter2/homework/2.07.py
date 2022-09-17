from math import sqrt
from turtle import *
length = 200
sum = 0
setheading(270)
while True:
    forward(length)
    sum += 1
    if (sum >= 3):
        break
    left(120)

up()
goto(pos()+(-length/6*sqrt(3), -length/2))
setheading(30)
down()

sum = 0
while True:
    forward(length)
    sum += 1
    if (sum >= 3):
        break
    right(120)

done()
