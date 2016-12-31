import turtle

def drawSprite(someturtle, numLegs, legLength):
    for legs in range(numLegs):
        someturtle.shape("circle")
        someturtle.stamp()
        someturtle.shape("classic")
        someturtle.left(360/numLegs)
        someturtle.forward(legLength)
        someturtle.stamp()
        someturtle.forward(-legLength)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    steve = turtle.Turtle()
    steve.pensize(3)
    steve.speed(8)
    steve.color("hotpink")

    drawSprite(steve, 15, 120)

    wn.exitonclick()

main()
