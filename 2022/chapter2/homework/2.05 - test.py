from turtle import *
sum = 0
while True:
    forward(200)
    sum = sum+1
    left(180-60)
    if (sum >= 3):
        break

setheading(60)
forward(100)
setheading(0)

sum = 0
while True:
    forward(100)
    sum = sum+1
    right(180-60)
    if (sum >= 3):
        break

done()
