#ex38.py

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #takes the last element off of more_stuff and saving it in next_one
    print("Adding:", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])    #starts with the end of the list
print(stuff.pop())
print(' '.join(stuff))  #prints list with a space in between
print('#'.join(stuff[3:5])) # object at index 3 up to but not including index 5
