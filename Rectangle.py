import turtle

turtle.Screen().bgcolor("orange")
sc = turtle.Screen()
sc.setup(500, 500)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()
board.color("Black")
board.begin_fill()
for i in range(2):
    board.forward(200)
    board.left(90)
    board.forward(100)
    board.left(90)
board.end_fill()
turtle.done()