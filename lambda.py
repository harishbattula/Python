# Lambda functions
'''
Lambda functions are anonimous functions
A lambda function evaluates an expression for a given argument. 
We give the function a value (argument) and then provide the operation (expression). 
The keyword lambda must come first. A full colon (:) separates the argument and the expression.
'''

# syntax of lambda function
# lambda argument : Expression

# normal function 
def Normal(c):
    return c+c

# print(Normal(2)) # 4

# lambda function
# print((lambda c : c+c)(2)) # 4

'''
In the code above, the function was created and then immediately executed. 
This is an example of an immediately invoked function expression or IIFE that runs as soon as it is defined.
'''

# usecases of lambda functions in filter and map inbuilt python libraries

NaturalNumbers = [i for i in range(1, 20)]

# filtering even numbers from the NaturalNumbers
EvenNumbers = filter(lambda x: x %2 == 0, NaturalNumbers)

# since filter method returns filter object, we need to encapsulate it using iterables
EvenNumbers = list(EvenNumbers)
print(EvenNumbers) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

OddNumbers = list(filter(lambda x: x%2 !=0, NaturalNumbers))
print(OddNumbers) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# using lambda in pandas dataframe
import pandas as pd
import numpy as np
data = {
    "Name" : ["manikanta", "fayaz ali", "pavan", "salman", "harish"],
    "Designation" : ["server administrator", "automation engineer", "hadoop admin", "salesforce developer", "data scientist"],
    "Company" : ["xyz", "abc", "def", "123", "jkl"],
    "DOBYear" : np.random.randint(low = 1994, high = 2000, size = 5),
    "Salary" : np.random.randint(low = 35000, high = 65000, size = 5)
}
df = pd.DataFrame(data) 
print(df.head())

# output
'''
        Name           Designation Company  DOBYear  Salary
0  manikanta  server administrator     xyz     1996   64757
1  fayaz ali   automation engineer     abc     1995   51896
2      pavan          hadoop admin     def     1997   56774
3     salman  salesforce developer     123     1998   39101
4     harish        data scientist     jkl     1994   60928
'''

# using map(apply) method with lambda on dataframe
df["Age"] = df["DOBYear"].apply(lambda x : 2022 - x)

print(df.head())

# output
'''        
        Name           Designation Company  DOBYear  Salary  Age
0  manikanta  server administrator     xyz     1996   64757   26
1  fayaz ali   automation engineer     abc     1995   51896   27
2      pavan          hadoop admin     def     1997   56774   25
3     salman  salesforce developer     123     1998   39101   24
4     harish        data scientist     jkl     1994   60928   28
'''

# filter by age using filter and lambda
print("age's greater than 25", list(filter(lambda x : x > 25, df["Age"])))

# output
# age's greater than 25 [26, 27, 28]

# captilizing first letter of each word in Name and Designation columns
df[["Name", "Designation"]] = df[["Name", "Designation"]].apply(lambda x : x.str.title())
print(df.head())

# output
'''
        Name           Designation Company  DOBYear  Salary  Age
0  Manikanta  Server Administrator     xyz     1996   64757   26
1  Fayaz Ali   Automation Engineer     abc     1995   51896   27
2      Pavan          Hadoop Admin     def     1997   56774   25
3     Salman  Salesforce Developer     123     1998   39101   24
4     Harish        Data Scientist     jkl     1994   60928   28
'''
