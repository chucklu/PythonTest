from turtle import *
import numpy as np
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
    color = tuple(np.random.randint(0,256,3))
    pencolor(color)
    circle(40, 80)

    color = tuple(np.random.randint(0,256,3))
    pencolor(color)
    circle(-40, 80)

color = tuple(np.random.randint(0,256,3))
pencolor(color)
circle(40, 80/2)
fd(40)

color = tuple(np.random.randint(0,256,3))
pencolor(color)
circle(16, 180)
fd(40 * 2/3)
done()