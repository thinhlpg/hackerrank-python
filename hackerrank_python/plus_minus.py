#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr_len = len(arr)
    num_of_postives = len([i for i in arr if i > 0])
    num_of_negetives = len([i for i in arr if i < 0])
    num_of_zeros = len([i for i in arr if i == 0])

    print('{:.6f}'.format(num_of_postives / arr_len))
    print('{:.6f}'.format(num_of_negetives / arr_len))
    print('{:.6f}'.format(num_of_zeros / arr_len))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
