import random

def contains_n(numbers, n):
    # Your code here, to replace this non-working version
    for x in numbers:
        if x == n:
            return True

    return False

#numList = [2, 4, 6, 3, 8, 10, 3.14, 5.4]
numList = []

for x in range(0, 10):
    number = random.randrange(0, 100)
    numList.append(number)

print(numList)

userN_str = input("Pick a number:")
userN = int(userN_str)

# Be sure to test your function with various inputs

if (contains_n(numList, userN)):
    print("Your number is in the list.")
else:
    print("Your number wasn't in the list.")
