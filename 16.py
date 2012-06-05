#!/usr/bin/env python

sum1 = 0
res = 2**1000
string = str(res)
for i in range(0,len(string)):
	sum1 = sum1 + int(string[i])
print sum1