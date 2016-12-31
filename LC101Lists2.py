import random
from test import testEqual

# The rollDice function simulates the rolling of the dice. It
# creates a 2 dimensional list: each column is a die and each
# row is a throw. The function generates random numbers 1-6
# and puts them in the list.
def rollDice(num_dice, num_rolls):

    # create a two-dimensional (num_dice by num_rolls) of zeros
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]

    # loop through each row and column, filling it with a random roll
    for roll in range(0, len(double_list)):
      for die in range(0, len(double_list[roll])):
          double_list[roll][die] = (int)(random.random()*6 + 1)

    return double_list


# This function takes a 2D list (which can be generated by rollDice)
# and sums the value of all the dice in each row. It returns a 1
# dimensional list with the sum of each throw.
# Example:
# double_list: [[1, 5, 6],[2, 3, 1],[1, 3, 3]]
# sumOfRoll should return: [12, 6, 7]
def sumOfRoll(double_list):
    # Your code here
    list = []
    for i in range(len(double_list)):
        sum = 0
        for j in range(len(double_list[i])):
            sum += double_list[i][j]
        list.append(sum)
    return list

# Bonus function! Takes a 2D list and returns
# the number of times a person rolls Yahtzee (all dice have
# the same value). Hint: you may want to create a helper
# function that takes individual rows of the list.
def yahtzee(double_list):
    # Bonus: your code here
    count = 0
    for i in range(len(double_list)):
        if helper(double_list[i]):
            count += 1
    return count


def helper(list):
    test = True
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            test = True
        else:
            return False
    return True
# To play, yo'd do something like this
# dice = input("How many dice?")
# rolls = input("What is the number of rolls?")
# list = rollDice(dice, rolls)
# print("Sum of roll:", sumOfRoll(list))

print("Testing sumOfRoll...")
testEqual(sumOfRoll([[4, 5, 2],[6,2,1],[4,4,4]]), [11, 9, 12])
testEqual(sumOfRoll([[3, 4, 6],[2,6,1],[3,4,3]]), [13, 9, 10])
print("Testing yahtzee...")
testEqual(yahtzee([[4, 5, 2],[6,2,1],[4,4,4]]), 1)
testEqual(yahtzee([[3, 4, 6],[2,6,1],[3,4,3]]), 0)
