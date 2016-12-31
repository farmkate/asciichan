import turtle

def drawStar(someturtle, somesize, somepoints):
    for length in range(somepoints):
        someturtle.forward(somesize)
        someturtle.right(180* (somepoints-1)/somepoints)

def move(someturtle):
    someturtle.up()
    someturtle.forward(300)
    someturtle.left(144)
    someturtle.down()

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    bob = turtle.Turtle()
    bob.color("hotpink")
    bob.shape("classic")
    bob.speed(8)
    bob.pensize(3)
    bob.up()
    bob.forward(-100)
    bob.down()

    for numStars in range(5):
        drawStar(bob, 100, 7)
        move(bob)
    wn.exitonclick()

main()
