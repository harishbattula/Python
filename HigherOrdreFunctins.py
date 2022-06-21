'''
This class is all about higher order Functions
Definition : Functions that accepts another function as parameter, or returns another function are called as Higher Order Functions.
Usually functions that deals with another function are known as higher order functions.
'''
# sample funtion
from ast import Expression
import re


def hello():
    print("hello")

# hello() 
# hello

# yell = hello 
# # creates reference for hello, and assigns it to variable, but not calls the function


# yell() 
# hello

# yell1 = hello

# yell1() 
# we can create multiple references of a function.


# passing function as an argument

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def Greet(func, text):
    
    Greetings = func(text)
    print(Greetings)

# Greet(whisper, "Hello everyone how are you!!")
# hello everyone how are you!!

# Greet(shout, "Hello everyone how are you!!")
# HELLO EVERYONE HOW ARE YOU!!


# returning function

def CreateAdder(x):
    def Adder(y):
        return x+y
    return Adder

Add100 = CreateAdder(100)

# print(Add100(50))
# 150

# Decorators

''' 
Decorators are a very powerful and useful tool in Python since it allows programmers 
to modify the behaviour of a function or class. 
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
without permanently modifying it 
'''

def ReturnWrapper(func):
    def Wrapper():
        print("This is the entrance in wrapper")
        func()
        print("End of wrapper function")
    return Wrapper

def hello():
        print("hello world")

Wrapper = ReturnWrapper(hello)
# Wrapper()

# sample output
# This is the entrance in wrapper
# hello world
# End of wrapper function




