from random import random
from turtle import *
import numpy as np

def randomColor():
    color = tuple(np.random.randint(0,256,3))
    print(color)
    return color

setup(650, 350, 200, 200)

# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)

penup()
fd(-250)
pendown()

pensize(25)
seth(-40)

for i in range(4):
    color = randomColor()
    pencolor(color)
    circle(40, 80)

    color = randomColor()
    pencolor(color)
    circle(-40, 80)

color = randomColor()
pencolor(color)
circle(40, 80/2)

color = randomColor()
pencolor(color)
fd(40)

color = randomColor()
pencolor(color)
circle(16, 180)

color = randomColor()
pencolor(color)
fd(40 * 2/3)

done()