#!/usr/bin/python3

class Person:

    def __init__(self, name):
        self.name = name

    def intro(self):
        print("Hello, Im {0}".format(self.name))

    def __str__(self):
        return self.name


if __name__ == "__main__":

    person1 = Person('alireza')
    person1.intro()
    print(person1)
