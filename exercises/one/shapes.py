from turtle import Turtle, exitonclick

tess =  Turtle()
#tess.shape("turtle")
tess.forward(300)
tess.color('red')
tess.shape('square')
for i in range(4):
    tess.forward(200)
    tess.left(90)
for i in range(4):
    tess.left(60)
    tess.forward(90)


exitonclick()