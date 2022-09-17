from turtle import *
sum = 0
while True:
    forward(200)
    sum = sum+1
    left(180-60)
    if (sum >= 3):
        break
done()
