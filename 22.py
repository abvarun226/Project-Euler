#!/usr/bin/env python

import sys

alpha = [0, 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for line in sys.stdin:
	line = line.replace("\"","")
	names = line.split(",")
names.sort()
j=1
score = []
for name in names:
	sum1 = 0
	for i in name:
		sum1 = sum1+alpha.index(i)
	prod = sum1 * j
	score.append(prod)
	j=j+1
print sum(score)