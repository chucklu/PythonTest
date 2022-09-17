# 正N边形的绘制
from turtle import *

count=3

def drawN(n):
    begin_fill()
    temp = 180*(n-2)/n
    angle = 180 - temp
    while True:
        forward(200)
        print(angle)
        right(angle)
        #print("position:{}, heading:{}".format(pos(),heading()))
        if (abs(pos())) < 1:
            break
    end_fill()

fillcolor("red")
while count<10:
    drawN(count)
    count+=1

done()
