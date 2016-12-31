#LC101counting.py

string = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus.')
stringList = list(string)
print(stringList)
letterDictionary = {}

for char in stringList:
    if char in letterDictionary:
        letterDictionary[char] = letterDictionary[char] + 1
    else:
        letterDictionary[char] = 1

for (k, v) in letterDictionary.items():
    print(k + ':', v)
