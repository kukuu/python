from turtle import Turtle, exitonclick

forwardA = 300
forwardB = 200
forwardC = 90
#rightangle
leftA = 90


tess =  Turtle()
#tess.shape("turtle")
tess.forward(forwardA)
tess.color('red')
tess.shape('square')
for i in range(4):
    tess.forward(forwardB)
    tess.left(leftA)
for i in range(4):
    tess.left(leftA)
    tess.forward(forwardC)


exitonclick()