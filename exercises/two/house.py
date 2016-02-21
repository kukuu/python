from turtle import Turtle, exitonclick

tess = Turtle()
tess.shape("turtle")

number_of_houses = 5

def square():
	for i in range(4):
		tess.forward(100)
		tess.right(90)

def triangle():
	tess.left(45)
	tess.forward(72.5)
	tess.right(90)
	tess.forward(72.5)

def reset_location():
	tess.right(45)
	tess.forward(100)
	tess.left(90)
	tess.forward(100)

def house():
	square()
	triangle()
	reset_location()

for i in range(number_of_houses):
	house()

exitonclick()