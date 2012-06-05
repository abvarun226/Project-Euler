#!/usr/bin/env python

import sys

sum=0
for line in sys.stdin:
	sum = sum + int(line)
string = str(sum)
print string[0:10]