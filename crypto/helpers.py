#helpers.py

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(letter):
    '''takes parameter letter and returns the index of that letter in the alphabet'''
    lowLetter = letter.lower()
    index = ALPHABET.index(lowLetter)
    return index


def rotate_character(char, rot):
    '''take a char and rot as parameter and returns index of the rotated letter in the amphabet'''
    return ALPHABET[(char + rot) % 26]
