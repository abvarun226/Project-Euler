#!/usr/bin/env python

i=1
num=0
while True:
	num = num + i
	i = i+1
	div = 0
	for j in range(2,int(num**0.5)):
		if num % j==0:
			div = div + 2
	div = div+2
	if div > 500:
		print num
		break