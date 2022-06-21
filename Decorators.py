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
Wrapper()

# sample output
'''
This is the entrance in wrapper
hello world
End of wrapper function
'''

# use cases of decorators

from time import time, sleep

def SumOfNumbers1(Number):
    sum = 0
    for i in range(Number+1):
        sum += i
    return sum

def SumOfNumbers2(Number):
    return Number*(Number+1) // 2

start = time()
sleep(1)
sum = SumOfNumbers1(10000000)
end = time()
print("Time taken for SumOfNumbers1 function is : ", end-start)
# time taken for SumOfNumbers1 is :  1.3324577808380127

start = time()
sleep(1)
sum = SumOfNumbers2(10000000)
end = time()
print("Time taken for SumOfNumbers2 function is : ", end-start)
# time taken for SumOfNumbers2 is :  1.0116219520568848

# we can modify the behaviour of the functions using decorators by wrapping another function.
def TimeIt(func):
    def Wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        sleep(1)
        end = time()
        print("time taken for "+func.__name__+" is : ", end - start)
    return Wrapper

@TimeIt
def SumOfNumbers1(Number):
    sum = 0
    for i in range(Number+1):
        sum += i
    return sum

@TimeIt
def SumOfNumbers2(Number):
    return Number*(Number+1) // 2

SumOfNumbers1(10000000)
# time taken for SumOfNumbers1 is :  1.3324577808380127

SumOfNumbers2(10000000)
# time taken for SumOfNumbers2 is :  1.0116219520568848

  
  
