'''
The filter() method filters the given sequence with the help of a function 
that tests each element in the sequence to be true or not.
'''

# syntax
'''
filter(function, sequence)
    Parameters:
        function: function that tests if each element of a sequence true or not.
        sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
    Returns:
        returns an iterator that is already filtered.
'''

def Even(Number):
    if Number%2 == 0:
        return True
    return False

SampleList = [1,2,3,4,5,6,7,87,99]

Filtered = filter(Even, SampleList)

'''
Note that the filter function returns a Filter object and we need to encapsulate it with a list to return the values.
'''

Filtered = list(Filtered)

print(Filtered)
# [2, 4, 6]

# Applications 
'''
It is normally used in lambda functions to seperate list, sets or tuples
'''

# above approach using lambda functions

Filtered = list(map(lambda x : x * x, SampleList))

print(Filtered)
# [2, 4, 6]
