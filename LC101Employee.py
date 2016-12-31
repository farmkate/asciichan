from LC101PersonClass import Person

class Employee(Person):
    def __init__(self, first, last, salary):
        super().__init__(first, last)
        self.salary = salary

    def get_name(self):
        return self.last_name + ', ' + self.first_name

    def get_salary(self):
        return self.salary

def main():
    p = Person('Bart', 'Simpson')
    print(p.get_name())

    p.first_name = 'Lisa'
    print(p.get_name())

    e = Employee('Homer', 'Simpson', '400000')
    print(e.get_name())
    print(e.get_salary())

    print(isinstance(p, Person))    #True
    print(isinstance(p, Employee))  #False

    print(isinstance(e, Person))    #True
    print(isinstance(e, Employee))  #True

if __name__ == '__main__':
    main()
