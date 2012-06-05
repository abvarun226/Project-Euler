#!/usr/bin/env python

ones_w = [0,'one','two','three','four','five','six','seven','eight','nine',0, 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ones = [0,3,3,5,4,4,3,5,5,4,0,6,6,8,8,7,7,9,8,8]
#ten_twenty = [0, 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
#ten_twenty = [0,6,6,8,8,7,7,9,8,8]

tens_w = [0,'ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
tens = [0,3,6,6,5,5,5,7,6,6]

hundred_ones_w = [0,'one','two','three','four','five','six','seven','eight','nine','ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hundred_ones = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]

hundreds_w = [0,'hundred']
hundreds = [0,7]

mem_w = {}
mem = {}
total = 0
for i in range(1,1001):
	#1 to 19
	if i < 20 and i != 10:
		total = total + ones[i]
		print ones_w[i]
		mem[i] = ones[i]
		mem_w[i] = ones_w[i]
		
	#11 to 19
	#elif i > 10 and i < 20:
	#	total = total + ten_twenty[i%10]
	
	#21 to 99 excluding 10,20,30, ..., 90
	elif i > 20 and i < 100 and i%10 != 0:
		total = total + tens[int(i/10)] + ones[i%10]
		print tens_w[int(i/10)] , ones_w[i%10]
		mem[i] = tens[int(i/10)] + ones[i%10]
		mem_w[i] = tens_w[int(i/10)] + " " + ones_w[i%10]
		
	#10,20,30, ...,90
	elif i < 100 and i%10 == 0:
		total = total + tens[i/10]
		print tens_w[i/10]
		mem[i] = tens[i/10]
		mem_w[i] = tens_w[i/10]
		
	elif i%100 == 0 and i<1000:
		total = total + ones[int(i/100)] + hundreds[1]
		print ones_w[int(i/100)], hundreds_w[1]
		
	elif i > 100 and i%100!=0:
		total = total + ones[int(i/100)] + hundreds[1] + 3 + mem[i%100]
		print ones_w[int(i/100)], hundreds_w[1], "and", mem_w[i%100]
		
total = total + 3 + 8
print "one thousand"
print total