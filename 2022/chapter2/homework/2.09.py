import imp
from turtle import *
import numpy as np

sum = 0
step = 40
length = 40
count = 0

def randomColor():
    color = tuple(np.random.randint(0,256,3))
    print(color)
    return color

pensize(25)
left(90)

sum=0
while True:
    circle(length, 180)
    print(heading())
    circle(length*2, 180)
    print(heading())
    sum+=1
    if(sum>=10):
        break
# while True:
#     if (count >= 2):
#         length += step
#         count = 0
#     left(180)
#     circle(length,180)
#     count = count+1
#     sum += 1
#     if (sum >= 39):
#         break
done()
