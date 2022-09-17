# 正五角星的绘制
from turtle import *
fillcolor("red")
print("position:{}, heading:{}".format(pos(),heading()))
left(180+72)
print("position:{}, heading:{}".format(pos(),heading()))
begin_fill()
while True:
    forward(200)
    left(144)
    print("position:{}, heading:{}".format(pos(),heading()))
    if (abs(pos())) < 1:
        break
end_fill()
