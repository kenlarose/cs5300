"""
Create a new file named task2.py demonstrating the use of various 
data types, including integers, floating-point numbers, strings, 
and boolean. Implement a Python using pytest to test case for each
data type, ensuring that the script’s behavior matches the expected 
outcomes.
"""

# basic arithmetic for demonstrating behavior of ints and floats
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def standard_divide(x, y):
    return x / y

def floor_divide(x, y):
    return x // y


# some string built-ins
def concatenate(text1, text2):
    return text1 + text2

def find_index_of(text, sub_string):
    return text.find(sub_string)

def get_slice(text, startIdx, endIdx): 
    return text[startIdx:endIdx]

def split_string(text, split_arg=None):
    return text.split(split_arg)


# some logical operations for booleans
def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_xor(a, b):
    return a ^ b

def logical_not(a):
    return not a