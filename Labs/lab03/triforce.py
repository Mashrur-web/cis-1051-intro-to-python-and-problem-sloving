import turtle

wn = turtle.Screen()
wn.bgcolor("white")

mat = turtle.Turtle()
mat.color("black")
mat.shape("turtle")
mat.shapesize(2, 2)


ben = turtle.Turtle()
ben.color("black")
ben.shape("turtle")
ben.shapesize(1, 1)

side = 130

num_of_sides = int(3)
angle = 360 / num_of_sides

mat.pendown()
for _ in range(num_of_sides):
    mat.left(angle)
    mat.forward(side)

ben.pendown()
ben.backward(side)
ben.left(60)
ben.fd(side / 2)
ben.right(60)

for _ in range(num_of_sides):
    ben.forward(side / 2)
    ben.right(angle)


ben.hideturtle()
mat.hideturtle()
turtle.done()
