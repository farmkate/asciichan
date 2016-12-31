import turtle
import random


def reverseList(list):
    newlist = []
    if len(list) <= 1:
        return list[0]
    else:
        return list[len(list)-1:] + [reverseList(list[:len(list)-1])]

testList = [2,5,'cat', 'dog', 9, 222]

print(reverseList(testList))


def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5))



def tree(branchLen,t):
    if branchLen > 5:
        angle = branchAngle()
        t.color(branchColor(branchLen))
        t.pensize(branchThickness(branchLen))
        t.forward(branchLen)
        t.right(angle)
        tree(branchLength(branchLen),t)
        t.color(branchColor(branchLen))
        t.pensize(branchThickness(branchLen))
        t.left(angle * 2)
        tree(branchLength(branchLen),t)
        t.color(branchColor(branchLen))
        t.pensize(branchThickness(branchLen))
        t.right(angle)
        t.penup()
        t.backward(branchLen)
        t.pendown()

def branchLength(branchLen):
    return branchLen - random.randint(5, 16)

def branchAngle():
    return random.randint(15, 46)

def branchThickness(branchLen):
    thick = 0
    if branchLen > 50:
        thick = 8
    elif branchLen > 25:
        thick = 6
    else:
        thick = 4
    return thick


def branchColor(branchLen):
    color = ''
    if branchLen > 50:
        color = 'brown'
    elif branchLen > 25:
        color = 'lightgreen'
    else:
        color = 'pink'
    return color


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()


def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))
print(toStr(10,2))

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[len(s)-1:] + reverse(s[:len(s)-1])

print(reverse('hello'))
print(reverse('l'))
print(reverse('follow'))
print(reverse(''))

def removeWhite(s):
    s.lower()
    newS = ''
    for char in s:
        if char.isalpha():
            newS = newS + char
    return newS


def isPal(s):
    if s == reverse(s):
        return True
    else:
        return False

print(isPal(removeWhite('x')))
print(isPal(removeWhite('radar')))
print(isPal(removeWhite('hello')))
print(isPal(removeWhite('')))
print(isPal(removeWhite('hannah')))
print(isPal(removeWhite("madam i'm adam")))
