#LC101oop.py

class Point:
    '''Point class for representing and manimpulating x,y coordinates'''

    def __init__(self, initX, initY):
        '''Create a new point at the given coordinates.'''
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distranceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  #determines what will print for an object in a print statement
        return 'x=' + str(self.x) + ', y=' + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distanceFromOrigin(self, target):
        return (((self.x - target.x) ** 2) + ((self.y - target.y) ** 2)) ** 0.5

    def reflect_x(self):
        reflextY = self.getY() * -1
        return Point(self.getX(), reflectY)

    def slopeFromOrigin(self):
        if self.getX() == 0:
            return (self.getY() - 0)/(self.getX() - 0)
        else:
            return None

    def slopeFromTwoPoints(self, target):
        if self.getX() - target.getX() == 0:
            return (self.getY() - target.getY())/(self.getX() - target.getX())
        else:
            return None

    def get_line_to(self, target):
        #y = mx + b
        #b is the Y intercept where the line crosses the Y axis
        #m is the slope
        m = int(self.slopeFromTwoPoints(target))
        b = int(self.getY() - (self.getX() * m))
        return Point(m, b)

    def move(self, dx, dy):
            self.x = self.getX() + dx
            self.y = self.getY() + dy
            return (Point(self.x, self.y))

point = Point(20, 20)
print(point)
point.move(5, -5)
print(point)

print(Point(4, 11).get_line_to(Point(6, 15)))




p = Point(7, 6)
print(p)

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY))


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def add(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)


myfraction = Fraction(12, 16)

print(myfraction)
myfraction.simplify()
print(myfraction)



def sameFraction(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)
print(sameFraction(myfraction, yourfraction))
