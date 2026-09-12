import turtle

james = turtle.Turtle()
james.shape("turtle")
james.pensize(3)


james.up()
james.back(200)
james.down()

james.left(90)
james.forward(100)


james.left(45)
james.forward(-80)

james.left(90)
james.forward(-80)


james.right(135)
james.forward(-90)
james.penup()


james.goto(0, 30)
james.left(90)
james.forward(-80)
james.pendown()
james.circle(120, 180)

james.hideturtle()
turtle.done()
