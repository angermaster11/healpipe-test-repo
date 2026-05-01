import numpy as np

def add(a, b):
    # Use Python's built-in addition for generality, avoids np.add type errors with strings
    return a + b

def divide(a, b):
    return np.divide(a, b)

