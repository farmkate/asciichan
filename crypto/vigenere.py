from helpers import alphabet_position, rotate_character


UALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(text, code):
    cipher = ''
    codeLength = len(code)
    j = 0

    for char in text:
        if j == codeLength:
            j = j % codeLength
        if char.isalpha():
            newCharIndex = alphabet_position(char)
            newCodeIndex = alphabet_position(code[j])
            rot = ord(code[j])
            newChar = rotate_character(newCharIndex, newCodeIndex)
            if char in UALPHABET:
                cipher = cipher + newChar.upper()
            else:
                cipher = cipher + newChar
            j += 1
        else:
            cipher = cipher + char
    return cipher


def main():
    phrase = input("Type a message: ")
    code = input("Excryption key: ")
    return encrypt(phrase, code)


if __name__== '__main__':
    main()
