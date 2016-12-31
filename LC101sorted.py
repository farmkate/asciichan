#LC101sorted.py

def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """
    # TODO: Fill in details
    for i in range(len(string)-1):
        if string[i] > string[i+1]:
            return False
    return True

print(is_sorted("ABC"))
print(is_sorted("aBc"))
print(is_sorted("dog"))
print(is_sorted("Apatania"))
