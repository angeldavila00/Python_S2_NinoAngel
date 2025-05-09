#!/bin/python3
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    total = sum(arr)
    min_num = min(arr)
    max_num = max(arr)
    
    min_sum = total - max_num
    max_sum = total - min_num
    
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)