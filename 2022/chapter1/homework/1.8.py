# 太阳花的绘制
from turtle import *
setposition(-200,0)
color('red', 'yellow')
sum = 0
begin_fill()
while True:
    forward(400)
    sum = sum+1
    #left(170)  # 10,所以会绘制36次
    left(175) # 5度,绘制360/5=72次
    print("{},{},{}".format(sum,pos(),abs(pos())))
    if (abs(pos())) < 1:
        break
end_fill()
print("sum = {}".format(sum))
