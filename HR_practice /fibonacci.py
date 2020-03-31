#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibonacci' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.

def fibonacci(n):
    # print(n)
    # Base Case of 0 and 1 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 


def fibArray(n):
    arr = []
    for i in range(n):
        arr.append(fibonacci(i))
    return arr



# print(fibonacci(1))       
# print(fibonacci(2))
# print(fibonacci(3))  
print(fibArray(10))