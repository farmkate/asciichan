#LC101inheritance.py


class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


# TODO define a class called BoredChatbot

class BoredChatbot(Chatbot):

    def response(self, prompt_from_human):

        if len(prompt_from_human) > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return Chatbot.response(self, prompt_from_human)

# make a bored chatbot
emma = BoredChatbot("Emma")
# introduce the chatbot and allow the user to say something
human_message = input(emma.greeting())
# respond to the user
print(emma.response(human_message))



class Cat:

    def __init__(self):
        # every Cat comes into this world tired and hungry
        self.tired = True
        self.hungry = True

    def sleep(self):
        self.tired = False
        # a Cat always wakes up hungry
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            # eating when already full makes a Cat sleepy
            self.tired = True

    def noise(self):
        # sleepy cats say prrrr, energized cats say meow!
        if self.tired:
            return "prrrr"
        else:
            return "meow!"

class Tiger(Cat): # notice the (Cat) in parentheses

    def angry(self):
        # a Tiger is angry whenever it is both hungry and tired
        return self.tired and self.hungry

    def noise(self):
        if self.angry():
            # an angry Tiger says GRRRR!
            return "GRRRR!"
        else:
            # a non-angry Tiger behaves like a Cat
            return Cat.noise(self)


hobbes = Tiger()
print("hobbes says:", hobbes.noise())
hobbes.sleep()
print("After sleeping, hobbes says:", hobbes.noise())
hobbes.eat()
print("After eating, hobbes still says:", hobbes.noise())
hobbes.eat()
print("After eating again, hobbes says:", hobbes.noise())



class HouseCat(Cat):

    def __init__(self, name):
        # first, initialize as a normal Cat
        Cat.__init__(self)
        # then set the name attribute
        self.name = name

    def satisfied(self):
        return not self.hungry and not self.tired

    def noise(self):
        if self.satisfied():
            return "Hello, my name is " + self.name + "!"
        else:
            return Cat.noise(self)

garfield = HouseCat("Garfield")
print("garfield says:", garfield.noise())
garfield.sleep()
print("After sleeping, garfield says:", garfield.noise())
garfield.eat()
print("After eating, garfield says:", garfield.noise())
garfield.eat()

tom = Cat()
print("tom says:", tom.noise())
tom.sleep()
print("After sleeping, tom says:", tom.noise())
tom.eat()
print("After eating, tom still says:", tom.noise())
tom.eat()
print("After eating again, tom says:", tom.noise())



import turtle

class StarTurtle(turtle.Turtle):

    def star(self, numpoints, radius):
        for i in range(0, numpoints):
            self.forward(radius)
            self.back(radius)
            self.left(360 / numpoints)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = StarTurtle()
tess.color("hotpink")

# draw a star
tess.star(7, 60)

# move somewhere else
tess.penup()
tess.forward(30)
tess.left(45)
tess.pendown()

# draw another star
tess.color("blue")
tess.star(15, 45)

# and one more
tess.color("yellow")
tess.star(15, 30)
