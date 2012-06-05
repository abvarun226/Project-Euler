#!/usr/bin/env python

flag=0
for i in range(1,1000):
	for j in range(i+1,1000):
		c = i**2 + j**2
		check = int(c**0.5)
		if check**2 == c:
			#print i, j, check
			if i+j+check==1000:
				print i,j,check
				print i*j*check
				flag=1
		if flag==1:
			break
	if flag==1:
		break