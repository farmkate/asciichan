#def testEqual(fuctionResult, expected):
#    if functionResult == expected:
#        result = 'Pass'
#    else:
#        result = 'Fail'
#    return result

def testEqual(a, b):
    if a == b:
        print('Pass:', a, '==', b)
    else:
        print('Fail:', a, '!=', b)
