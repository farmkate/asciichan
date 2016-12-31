class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def get_name(self):
        return self.first_name + ' ' + self.last_name



def main():
    p = Person('Homer', 'Simpson')
    print(p.get_name())

if __name__ == '__main__':
    main()
