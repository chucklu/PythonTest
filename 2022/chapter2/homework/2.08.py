from turtle import *
sum = 0
step = 10
length = 10
count = 0
while True:
    if (count >= 2):
        length += step
        count = 0
    left(90)
    forward(length)
    count = count+1
    sum += 1
    if (sum >= 83):
        break
done()
