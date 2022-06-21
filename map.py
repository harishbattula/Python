'''
map function returns the map object, after mapping each item in iterable or 
multiple iterables using passed function
'''

# Syntax
'''
map(function, iterable)
or
map(function, iterable1, iterable2)

parameters :
    function : function that maps the each item by considering logic
    iterables : any iterable list, tuple or sets...
returns : map function returns map object, we need to encapsulate using list or set..
'''

# examples 
def Add(Number):
    return Number + Number

SampleList1 = [1, 2, 3, 4, 5]

MappedList = map(Add, SampleList1)

MappedList = list(MappedList)

print(MappedList) # [2, 4, 6, 8, 10]

# mapping with lambda function
MappedList = map(lambda x : x + x, SampleList1)
MappedList = list(MappedList)

print(MappedList) # [2, 4, 6, 8, 10]

# mapping with multiple iterables
SampleList2 = [6, 7, 8, 9, 10]
MappedList = list(map(lambda x, y : x + y, SampleList1, SampleList2))

print(MappedList) # [7, 9, 11, 13, 15]

# mapping using inbuilt functions
Members = ["mani", "fayaz", "pavan"]
MappedList = list(map(list, Members))

print(MappedList) # [['m', 'a', 'n', 'i'], ['f', 'a', 'y', 'a', 'z'], ['p', 'a', 'v', 'a', 'n']]
