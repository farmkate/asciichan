#LC101rot13.py

def rot13(mess):
    # Your code here
    rotate = 13
    cipher = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in mess:
        if char.isalpha():
            index = alphabet.index(char)
            cipher = cipher + alphabet[(index + rotate) % 26]
        else:
            cipher = cipher + char
    return cipher

print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('since rot13 is symmetric you should see this message')))
