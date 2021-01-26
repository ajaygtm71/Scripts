#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(str):
    n =len(str)
    if n==1: return str
    if n==0:  return "Empty String"
    i=0
    prefix = ''
    suffix = ''
    for i in range(n-1):
        if str[i]==str[i+1]:
            if i>0:
                prefix = str[:i]
            if i<n-2:
                suffix = str[i+2:]
            break
    if i==n-2 and str[i]!=str[i+1]:
        pass
    else:
        str = superReducedString(prefix+suffix)
    return str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
