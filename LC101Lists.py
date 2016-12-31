#chapter 11

def countLength(lst, length):
    count = 0
    for word in lst:
        if len(word) == length:
            count += 1
    return count

list = ['earth', 'dog', 'heart', 'he']

print(countLength(list, 5))

def countKey(lst,key):
    count = 0
    for word in lst:
        count += 1
        if word == key:
            return count
    return count

list = ['earth', 'dog', 'heart', 'sam', 'he']

print(countKey(list, 'sam'))


def replace(s, old, new):
    list = s.split(old)
    return(new.join(list))

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
print(replace(s, 'om', 'am'))
print(replace(s, 'o', 'a')    )
print(replace('Mississippi', 'i', 'I'))
