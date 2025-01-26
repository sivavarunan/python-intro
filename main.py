print("Hello World")

# #is used for writing comment in python

"""
Long line of comment
indentation is important in python
Python is case sensitive
"""

# creating Variables
x = 10
deci = 10.212
name = "siva"
Name = 'eren'
active = True

"""
variables doses not need to be declared with any particular type
to specify datatype can be done using casting
String variables can be declared using either single or double quotes
variable names are case sensitive
"""

y = str(10)
z = int(2)
a = float(3)

"""
'print' is used to output in terminal
'type' is used to get the data type of the variable
"""

print(type(y))       # output <class 'str'>

"""
There are some rules for variable names
1. must start with letter or underscore character
2. name cannot start with number
3. only can contain (A-z , 0-9 and _ )
4. names are case sensitive
5. cannot be any python keywords
Proper ways to write multi words variables names
"""

# 1.Camel Case - each word except the first, starts with capital
myVariableName = "krishna"

# 2.Pascal Case - each word start with capital letter
MyVariableName = "krishna"

# 3.Snake Case - each word is separated by underscore
my_variable_name = "Krishna"

"""
Assigning many values to multiple variables in one line
also possible to assign single value to multiple variables
also can be used to unpack a collection
"""
fruit1, fruit2, fruit3 = "apple", "banana", "orange"
f1 = f2 = f3 = "orange"

"""
out put variables using 'print' function 
multiple variables can be printed using ,
'+' is also used to print multiple variables
'+' is used as add in numbers
there will be error if you try to  print number and string together using '+'
"""

# Global variables
variable = "awesome"


def myfunc():
    global v
    v = "great"
    print("python is " + variable)


myfunc()

print("python is " + v)

"""
variables that are created outside the function is global variables
you can create variable locally also
'global' keyword is used in function to define variable globally

"""