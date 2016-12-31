#LC101removeAll.py
def remove_all(substr,theStr):
    # your code here
    test = theStr.find(substr)
    #first = theStr.find(substr)
    newStr = theStr[test:]
    last = theStr.rfind(substr)
    beg = 0
    if test < 0:
        return theStr
    else:
        while(substr in newStr[last:]):
            last = last + len(substr)  #newStr[last + 1:].rfind(substr) #assigns the index when the substr begins
        return theStr[:test] + theStr[last:]

print(remove_all('an', 'banana'), '\t\tExpected: ba')
print(remove_all('cyc', 'bicycle'), '\tExpected: bile')
print(remove_all('iss', 'Mississippi'), '\tExpected: Mippi')
print(remove_all('eggs', 'bicycle'), '\tExpected: bicycle')
