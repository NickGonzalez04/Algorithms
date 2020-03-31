#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedBrackets' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING string as parameter.
#

def balancedBrackets(string):
    # Write your code here
    print(string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()

    result = balancedBrackets(string)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
