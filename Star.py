import turtle

turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()
board.color("Black")
board.begin_fill()
for i in range(5):
    board.forward(100)
    board.left(144)
board.end_fill()
turtle.done()