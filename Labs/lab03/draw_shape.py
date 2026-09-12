import turtle

wn = turtle.Screen()
wn.bgcolor("white")

mat = turtle.Turtle()
mat.color("black")
mat.shape("turtle")
mat.shapesize(2, 2)

side = 120

num_of_sides = int(input("Enter the number of sides: "))
angle = 360 / num_of_sides

mat.pendown()
for _ in range(num_of_sides):
    mat.left(angle)
    mat.forward(side)

mat.hideturtle()
turtle.done()
