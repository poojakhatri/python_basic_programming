#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSum(arr):
	n = len(arr)
	sum_1 = 0
	sum_2 = 0
 	

	for i in arr:
		
		sum_1 += i
		print(sum_1)
		sum_2 += arr[len(arr) -i]
		print(sum_2)

		if sum_1 == sum_2:
			return arr.index(len-i)
		
	# minpos = arr.index(min(arr)) 
	

arr_count = int(input().strip())

arr = []

for i in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)
print("elements:")
result = balancedSum(arr)
print(result)

