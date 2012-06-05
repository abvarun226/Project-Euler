#!/usr/bin/env python
"""From example problem, consider the penultimate row, specifically the triangle with 2 as apex and 8, 5 as the base. The maximum sum in this triangle is 2+8 =  10. Replace 2 with 10. Do the same for all the triangles formed with the penultimate layer as the apex. Refer http://blog.singhanuvrat.com/problems/project-euler-maximum-sum-traversing-top-to-bottom-in-a-triangle"""

def add(x,y):
	return x+y

sum1=0
rows = 15
temp = []
#num = [0, 3 ,7, 4, 2, 4, 6, 8, 5, 9, 3]
num = [0,75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,19,1,23,75,3,34,88,2,77,73,7,63,67,99,65,4,28,6,16,70,92,41,41,26,56,83,40,80,70,33,41,48,72,33,47,32,37,16,94,29,53,71,44,65,25,43,91,52,97,51,14,70,11,33,28,77,73,17,78,39,68,17,57,91,71,52,38,17,14,91,43,58,50,27,29,48,63,66,4,68,89,53,67,30,73,16,69,87,40,31,4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
for row in range(rows-1, 1, -1):
	index = reduce(add, range(1,row))
	for ele in range(index+1, index+1+row):
		temp1 = num[ele] + num[ele+row]
		temp2 = num[ele] + num[ele+row+1]
		if temp1 > temp2:
			ele_sum = temp1
			#print num[ele], "+", num[ele+row],"+"
		else:
			ele_sum = temp2
			#print num[ele], "+", num[ele+row+1],"+"
		temp.append(ele_sum)
	del num[index+1:]
	for i in temp:
		num.append(i)
	temp = []
temp1 = num[1]+num[2]
temp2 = num[1]+num[3]
if temp1 > temp2:
	print temp1
else:
	print temp2

