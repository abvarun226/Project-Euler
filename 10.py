#!/usr/bin/env python

import sys
from math import *

def sieve(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)
def add1(x,y):
	return x+y

is_prime = {}
lower = 2
upper = 2000000
res = sieve(upper)
print reduce(add1, res)