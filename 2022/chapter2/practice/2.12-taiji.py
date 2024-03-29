# 将一一分为二，就画出了半径为二分之一的两个圆弧，此为一生二，这两道圆将大圆分成了阴阳两部分，事物分成正反两方面
# 到了最关键的画阴阳眼了，将二分之一,一分为二,连分三次（也就是0.5*0.5*0.5=1/8），就画出了半径为八分之一的阴阳眼，阴阳眼的面积为π*1/64，刚好是大圆面积的64分之一，
# 暗合八八六十四卦，也就是二生三三生万物，也就是用八八六十四卦来类比天地万物。

# https://blog.csdn.net/weixin_42398141/article/details/112232589
# 先天太极八卦图的太极是顺时针旋转；阴阳鱼位置是：阳鱼在上，阴鱼在下，阴阳鱼眼在同一条水平线上
# 黑色表示属阴, 黑中白点表示阴中有阳.白色表示属阳, 白中黑点表示阳中有阴.

from turtle import *
radius = 300
up()
setpos(pos()+(-radius, 0))
down()

# 绘制阴鱼
begin_fill()
seth(270)
circle(radius, 180)
seth(270)
circle(-radius/2.0, 180)
circle(radius/2.0, 180)
end_fill()

# 绘制阳鱼
seth(90)
circle(-radius, 180)

# 绘制阴眼
up()
setpos(pos()+(-3/8.0*radius, 0))
down()
begin_fill()
circle(-1/8.0*radius)
end_fill()

up()
home()
setpos(pos()+(-3/8.0*radius, 0))
down()

# 绘制阳眼
fillcolor("white")
begin_fill()
seth(270)
circle(-1/8.0*radius)
end_fill()

done()
