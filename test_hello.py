#!/usr/bin/python3

import hello

def test_hello():
    person = hello.Person('alireza')
    return person

if __name__ == "__main__":
    person = test_hello()
    print(person)
