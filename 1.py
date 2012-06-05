#!/usr/bin/env python

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b, a % b)
def lcm(a,b):
	res = a * b/(gcd(a,b))
	return res

num = 1
for i in range(2,20):
	num = lcm(num,i)
print num