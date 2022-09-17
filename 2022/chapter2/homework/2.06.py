from turtle import *
l = 200
half = l/2
quarter = 200/4

forward(100)
up()

goto(pos()+(quarter, quarter))
setheading(90)
down()
forward(100)
up()

goto(pos()+(-quarter, quarter))
setheading(180)
down()
forward(100)
up()

goto(pos()+(-quarter, -quarter))
setheading(270)
down()
forward(100)

done()