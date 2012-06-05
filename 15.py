#!/usr/bin/env python
"""Solution here is using combinatorics. Can be solved using DP. Refer http://www.leetcode.com/2010/11/unique-paths.html"""

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
	
m=21
n=21
prod=1
for i in range(40, 20, -1):
	prod=prod*i
denom = fact(20)
print prod/denom