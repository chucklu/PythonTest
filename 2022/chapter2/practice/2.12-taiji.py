from turtle import *
radius = 300
up()
setpos(pos()+(0, -radius))
down()
circle(radius)
circle(radius/2.0, 180)
circle(-radius/2.0, 180)
done()
