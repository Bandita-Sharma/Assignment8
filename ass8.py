#Que1-->Name and handle the exception occured in the following program:
"""a=3
if a<4:
    a=a/(a-3)
    print(a)"""
"-->The exception in this program is ZeroDivisionError <--"
#PROGRAM TO HANDLE THE EXCEPTION:
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as message:
    print(message)
print()

#Que2-->Name and handle the exception occured in the following program:
"""l=[1,2,3]
print(l[3])"""
"-->The exception in this program is IndexError<--"
#PROGRAM TO HANDLE THE EXCEPTION:
try:
    l=[1,2,3]
    print(l[3])
except IndexError as message:
    print(message)
print()

#Que3-->What will be the output of the following code:
"""#Program to depict Raising Exception
     
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not"""

"-->THE EXCEPTION IN THE CODE IS :\
                                An exception\
                                NameError:Hi there<--"
print()

#Que4-->What will be the output of the following code:
"""# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    # Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)"""

"-->OUTPUT OF THE CODE IS:\
    -5.0 \
    a/b result in 0 <--"
print()

#Que5-->Write a program to show and handle following exceptions:1.ImportError 2.ValueError 3.IndexError
print("PROGRAM FOR ImportError:")
'''the ImportError is raised when an import statement has trouble \
    successfully importing the specified module.'''
import sys
try:
    from exception import myexception
except Exception as e:
    print(e)
print()

print("PROGRAM FOR ValueError:")
'''In Python , a value is the information that is stored within\
    a certain object. To encounter a ValueError in Python means that\
    is a problem with the content of the object you tried to assign\
    the value to'''

try:
    x=int(input("enter a number"))
    print(x)
except ValueError as message:
    print(message)
print()

print("PROGRAM FOR IndexError:")
'''It is raised whenever attempting to access an \
    index that is outside the bounds of a list'''
try:
    l=[1,2,3]
    print(l[3])
except IndexError as message:
    print(message)
print()
