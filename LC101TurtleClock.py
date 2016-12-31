import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
clock = turtle.Turtle()
clock.color("blue")
clock.shape("turtle")
clock.stamp()
for i in range(12):
    clock.penup()
    clock.forward(75)
    clock.pendown()
    clock.forward(10)
    clock.penup()
    clock.forward(10)
    clock.stamp()
    clock.forward(-95)
    clock.right(360/12)

wn.exitonclick()
