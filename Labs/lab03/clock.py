import turtle

wn = turtle.Screen()
wn.bgcolor("white")

chad = turtle.Turtle()
chad.color("pink")
chad.shape("turtle")
move = 30

for _ in range(12):
    chad.penup()
    chad.forward(50)
    chad.penup()
    chad.forward(50)
    chad.pendown()
    chad.forward(25)
    chad.penup()
    chad.forward(15)
    chad.stamp()
    chad.home()
    chad.right(move)
    move = move + 30

chad.hideturtle()
turtle.done()
