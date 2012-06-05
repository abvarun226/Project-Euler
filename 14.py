#!/usr/bin/env python

res = 9
chain = 20
for i in range(14,1000001):
	n = i
	j = 1
	while n!=1:
		j=j+1
		if n%2==0:
			n=n/2
		else:
			n=3*n+1
	if j > chain:
		chain = j
		res = i
print res