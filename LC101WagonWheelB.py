#LC101WagonWheelB.py
import turtle
import sys

def square(turtle, length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def quad(turtle, length):
    for i in range(4):
        turtle.left(90)
        square(turtle, length)

def wagonWheel(turtle, length, nlines):
    for i in range(nlines // 2):
        quad(turtle, length)
        turtle.right(180/nlines)


mike = turtle.Turtle()
mike.speed(9)

wagonWheel(mike, 100, 10)
