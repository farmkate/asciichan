#LC101removechar.py

#from test import testEqual

def remove_char(a_str, a_char):

    new_str = ''

    for idx in range(len(a_str)):
        if a_str[idx] != a_char:
            new_str = new_str + a_str[idx]

    return new_str

print(remove_char('aardvark', 'a'))
print('\tExpected: rdvrk')
print(remove_char('aardvark', 'k'))
print('\tExpected: aardvar')
print(remove_char('asdf', 'z'))
print('\tExpected: asdf')
print(remove_char('', 'a'))
print('\tExpected:  ')

def remove_letter(theLetter, theString):
    # your code here
    count = theString.count(theLetter)
    newString = ""

    if count > 0:
        for i in range(len(theString)):
            if theString[i] != theLetter:
                newString = newString + theString[i]
        return newString
    else:
        return theString


def remove(substr,theStr):
    # your code here
    beg = theStr.find(substr)
    if beg < 0:  #if substring not found in string
        return theStr
    return (theStr[:beg]+theStr[beg + len(substr):])

print(remove('an', 'banana'), '\tExpected: bana')
print(remove('cyc', 'bicycle'), '\tExpected: bile')
print(remove('iss', 'Mississippi'), '\tExpected: Missippi')
print(remove('egg', 'bicycle'), '\tExpected: bicycle')


def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels = sWithoutVowels + eachChar
    return sWithoutVowels

print(removeVowels("compsci"))
print(removeVowels("aAbEefIijOopUus"))



def remove_all(substr,theStr):
    # your code here
    print('remove_all function:')
    test = theStr.find(substr)
    newStr = ''
    shorter = ''
    i = 0
    if test < 0:
        return theStr
    else:
        beg = test
        for i in range(0, len(theStr) , len(substr)):
            shorter = theStr[i:beg] + theStr[beg + len(substr):]
            i = beg
        return shorter

print(remove_all('an', 'banana'), '\tExpected: ba')
print(remove_all('cyc', 'bicycle'), '\tExpected: bile')
print(remove_all('iss', 'Mississippi'), '\tExpected: Mippi')
print(remove_all('eggs', 'bicycle'), '\tExpected: bicycle')



def reverse(original):
    """Returns a reversed string"""
    reverse = ''
    for i in range(len(original)-1, -1, -1):
        reverse = reverse + original[i]

    return reverse

print(reverse("abcde"))


def reverse2(original):
    reverse = ''
    for in in range(len(original)):
        reverse - original[i] + reverse
    return reverse


def reverse3(original):
    reverse = ''
    for c in original:
        referse = c + reverse
    return reverse

def mirror(text):
    # your code here
    backwards = reversea(text)
    return text + backwards


def reversea(text):
    # your code here
    newStr = ''
    for c in text:
        newStr = c + newStr
    return newStr
