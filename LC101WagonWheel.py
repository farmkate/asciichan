#LCWagonWheel


import turtle

def draw_line(t, length, angle):
    t.left(angle)
    t.forward(length / 2)
    t.forward(-length)
    t.forward(length / 2)

def star(turtle, nlines, length):
    for angle in range(nlines):
        draw_line(turtle, 200, 180/nlines)

def outerSquare(turtle, nlines, length):
    turtle.forward(length / 2)
    turtle. right(90)
    turtle.forward(length / 2)
    turtle.right(90)
    for angle in range(nlines*2):
        turtle.forward(length)
        turtle.right(90+5)

def wagonWheel(turtle, nlines, length):
    star(turtle, nlines, length)
    outerSquare(turtle, nlines, length)

mike = turtle.Turtle()
mike.speed(8)

wagonWheel(mike, 10, 200)
