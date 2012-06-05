#!/usr/bin/env python

amicable = []
mem = {}
for n in range(2,10000+1):
	sum1=1
	m=n
	try:
		sum1 = mem[n]
	except KeyError:
		for i in range(1,int(m**0.5)):
			if m%i == 0:
				j=m/i
				if i!=m and j!=m:
					sum1=sum1+i+j
		mem[n] = sum1
	try:
		sum2 = mem[sum1]
	except KeyError:
		sum2=1
		m=sum1
		for i in range(1,int(m**0.5)):
			if m%i == 0:
				j=m/i
				if i!=m and j!=m:
					sum2=sum2+i+j	
		mem[m] = sum2
	if n == sum2 and n!=sum1:
		print n,sum1
		if n not in amicable:
			amicable.append(n)
		if sum1 not in amicable:
			amicable.append(sum1)
print sum(amicable)