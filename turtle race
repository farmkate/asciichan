import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

names = ["andy", "lance"]

# your code goes here
#for i in range(2):
#    andy.forward(random.randrange(100))
#    lance.forward(random.randrange(100))

andy.pendown()
lance.pendown()
for i in range(5, random.randrange(100, 500)):
    andy.forward(6)
    andy.left(5)
for i in range(5, random.randrange(100, 500)):
    lance.forward(6)
    lance.left(5)

wn.exitonclick()
