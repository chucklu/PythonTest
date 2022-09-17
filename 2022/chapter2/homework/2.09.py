from turtle import *
sum = 0
step = 40
length = 40
count = 0
pensize(25)
while True:
    if (count >= 2):
        length += step
        count = 0
    left(90)
    circle(length,180)
    count = count+1
    sum += 1
    if (sum >= 39):
        break
done()
