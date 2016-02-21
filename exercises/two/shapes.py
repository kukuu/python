from turtle import *

tess = Turtle()
tess.shape("turtle")

left = 45
forward = 35

while True:

    tess.left(left)
    tess.forward(forward)

    if abs(tess.pos()) < 1:
    	
    	break


exitonclick()