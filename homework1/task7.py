"""
Use pip package manager to add a Python package of your
choice to your project (e.g., requests, numpy, matplotlib).
Create a new file named task7.py and write a Python script 
that demonstrates how to use the chosen package to perform 
a specific task or function. Implement pytest test cases to
verify the correctness of your code when using the package.
"""

import numpy as np

def new_one_dimensional_array(length):
    return np.arange(length)

def get_array_attributes(array):
    return {
        "dimensions": array.ndim,
        "size": array.size,
        "shape": array.shape,
    }

def reshape_to_two_dimensions(array):
    return array.reshape(3, 3)
