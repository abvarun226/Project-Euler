#!/usr/bin/env python

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

num = fact(100)
print sum(map(int, str(num)))