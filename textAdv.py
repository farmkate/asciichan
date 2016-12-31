#textAdv.py
import random
import sys
import math

def boat(name):
    print(name + ", your adventure begins on the other boat.")


def island(name):
    print(name + ", your adventure begins on the island.")


def ocean(name):
    print(name + ", you start paddling toward the open ocean.")

    for i in range(random.randrange(5, 15)):
        if i % 2 == 0:
            print("You paddle for awhile and then turn aft.")
        else:
            print("You paddle for awhile and then turn starboard.")

    print("Now you are tired, so you go to sleep")
    exit()

def start():
    print("What is your name?")
    name = input(">> ")
    print("You are in a boat on the ocean.")
    print("You can paddle toward another boat, an island, or the open ocean.")
    print("Which do you choose?")

    first = input(">> ")

    if "boat" in first:
        boat(name)
    elif "island" in first:
        island(name)
    elif "ocean" in first:
        ocean(name)
    else:
        end("I don't know what you meant.")


start()
