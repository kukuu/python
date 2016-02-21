import turtle

tess = turtle.Turtle()

while True:
    move = input('\nType a w d s for left up right down (q to exit): ')
    if move == 's':
    	tess.setheading(270)
    	tess.forward(10)

    if move == 'a':
        tess.setheading(180)  # west
        tess.forward(10)

    if move == 'w':
    	tess.setheading(90)
    	tess.forward(10)

    if move == 'd':
    	tess.setheading(0)
    	tess.forward(10)

    if move == 'q':
        break