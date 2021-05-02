import numpy as np

def a(lst):
    b = 1
    for i in lst:
        b *= i
    return b
 
print(a([1, 2]))

