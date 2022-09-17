import imp
from operator import le
from turtle import *
import numpy as np

sum = 0
step = 20
length = 10


def randomColor():
    color = tuple(np.random.randint(0, 256, 3))
    print(color)
    return color


pensize(15)
left(90)

while True:
    length += step
    circle(length, 180)
    print(heading())

    length += step
    circle(length, 180)
    print(heading())

    sum += 1
    if (sum >= 3):
        break
done()
