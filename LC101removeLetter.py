#LC101removeLetter.py

from test import testEqual

def remove_letter(theLetter, theString):
    # your code here
    count = theString.count(theLetter)
    newString = ""
    begIndex = 0
    i = 0
    if count > 0:
        while i < count:  #for i in range(count):
            index = theString.find(theLetter)
            newString = newString + theString[begIndex:index]
            begIndex = index + 1
        return theString
    else:
        return theString


print(remove_letter('a', 'apple'))
print('Expect: pple')

print(remove_letter('a', 'banana'))
print('Expected: bnn')

print(remove_letter('z', 'banana'))
print('Expected: banana')
