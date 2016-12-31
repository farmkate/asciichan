from sys import argv, exit
#print("I know that these are the words the user typed on the command line: ", argv)
from helpers import alphabet_position, rotate_character

UALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def user_input_is_valid(cl_args):
    '''Testing whether the command line arguments are valid'''
    check = True
    if len(cl_args) != 2:
        check = False
        return check
    if not cl_args[1].isdigit():
        check = False
        return check
    return check



def encrypt(text, rot):
    '''takes text and rot as parameters and return encrypted text'''
    cipher = ''
    for char in text:
        if char.isalpha():
            newCharIndex = alphabet_position(char)
            newChar = rotate_character(newCharIndex, rot)
            if char in UALPHABET:
                cipher = cipher + newChar.upper()
            else:
                cipher = cipher + newChar
        else:
            cipher = cipher + char
    return cipher


def main():
    if not user_input_is_valid(argv):
        print("usage:  python3 carsar.py n")
        exit()
    phrase = input("Type a message: ")
    rotate = int(argv[1])
    return encrypt(phrase, rotate)


if __name__== '__main__':
    main()
