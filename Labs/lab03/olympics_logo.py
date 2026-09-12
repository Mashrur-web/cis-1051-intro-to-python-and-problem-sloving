import turtle

wn = turtle.Screen()
wn.bgcolor("white")
bob = turtle.Turtle()
bob.shape("turtle")
bob.pensize(3)
bob.penup()
bob.goto(-130, 30)
bob.pendown()
bob.color("blue")
bob.circle(60)

bob.penup()
bob.goto(0, 30)
bob.color("black")
bob.pendown()
bob.circle(60)

bob.penup()
bob.goto(130, 30)
bob.color("red")
bob.pendown()
bob.circle(60)


bob.penup()
bob.goto(-65, -30)
bob.color("orange")
bob.pendown()
bob.circle(60)

bob.penup()
bob.goto(65, -30)
bob.color("green")
bob.pendown()
bob.circle(60)

bob.hideturtle()
turtle.done()
