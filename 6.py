#!/usr/bin/env python

sum_square = 0
square_sum = 0
for i in range(1,101):
	sum_square = sum_square + i**2
	square_sum = square_sum +i
square_sum = square_sum**2
print square_sum-sum_square