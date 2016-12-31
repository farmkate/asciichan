import math

# convention class should capitalize the first letter of all words
class Point:
    ''' Point class for representing and manipulation x, y coordinates '''

    def __init__(self, x, y):
        ''' Create a new point '''
        self.x = x
        self.y = y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    #the == will be overidden by this // search implement equals character
    def __eq_(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

    # the != will be overidden by this
    def __ne__(self, other):
        return not self.__eq__(other)


    #accessor method
    def getX(self):
        return self.x

    #mutator method
    def setX(self, x):
        self.x = x

    #accessor method
    def getY(self):
        return self.y


    #mutator method
    def setY(self, y):
        self.y = y

    #by convention is it better to name methods with underscores between words
    def distance_from_origin(self):
        return ((self.x ** 2))  #not finished with this function

    def distance_from_point(self, point):
        retuurn distance(self.point)

#this function is not part of the Point class
def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist


def main():
    p = Point(1, 2)
    q = Point (5, 3)
    print(p)

    print(p.getX()) #using accessor
    print(p.x)          #direct access, the "python way"

    p.setX(3)
    print(p)

    p.x = 1     #direct access, the 'python way'
    print(p)

    p.count = 5     #you can create a new ___, but it is bad form, can be a problem is you type a name in wrong and create a new object or method

    r = Point(4, 5)
    s = r
    print( r is s)  #is checks object equality
    print(r == s)

if __name__ == '__main__':
    main()
