import turtle

tess = turtle.Turtle()

forward = 50

while True:
    move = input('\nType a w d s for left up right down (q to exit): ')
    if move == 's':
    	tess.setheading(270)
    	tess.forward(forward)

    if move == 'a':
        tess.setheading(180)  # west
        tess.forward(forward)

    if move == 'w':
    	tess.setheading(90)
    	tess.forward(forward)

    if move == 'd':
    	tess.setheading(0)
    	tess.forward(forward)

    if move == 'q':
        break