def get_initials(fullname):
    uppername = fullname.upper()
    initials = uppername[0]
    for i in range(1, len(uppername)):
        if uppername[i] == " ":
            initials = initials + uppername[i+1]
    return initials

def main():
    name = input("What is your full name? ")
    get_initials(name)


if __name__== '__main__':
    main()
