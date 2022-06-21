'''
Definition : Functions that accepts another function as parameter, or returns another function are called as Higher Order Functions.
Usually functions that deals with another function are known as higher order functions.
'''
# simple funtion
def hello():
    print("hello")

hello() 
# hello

yell = hello 
# creates reference for hello, and assigns it to variable, but not calls the function


yell() 
# hello

yell1 = hello

yell1() 
# we can create multiple references of a function.

# passing function as an argument

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def Greet(func, text):
    
    Greetings = func(text)
    print(Greetings)

Greet(whisper, "Hello everyone how are you!!")
# hello everyone how are you!!

Greet(shout, "Hello everyone how are you!!")
# HELLO EVERYONE HOW ARE YOU!!


# returning function

def CreateAdder(x):
    def Adder(y):
        return x+y
    return Adder

Add100 = CreateAdder(100)

print(Add100(50))
# 150
