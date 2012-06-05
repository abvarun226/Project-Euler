#!/usr/bin/env python

import resource

def memory_usage():
    """Memory usage of the current process in kilobytes."""
    status = None
    result = {'peak': 0, 'rss': 0}
    try:
        # This will only work on systems with a /proc file system
        # (like Linux).
        status = open('/proc/self/status')
        for line in status:
            parts = line.split()
            key = parts[0][2:-1].lower()
            if key in result:
                result[key] = int(parts[1])
    finally:
        if status is not None:
            status.close()
    return result

def get_day_code(year):
	x1 = int((year - 1)/ 4)
	x2 = int((year - 1)/ 100)
	x3 = int((year - 1)/ 400)
	day_code = (year + x1 - x2 + x3) %7
	return day_code

def get_leap_year(year):
	if (year%4 == 0 and year%100 != 0) or year%400 == 0:
		return True
	else:
		return False

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# day_code = [0=sunday ... 6=saturday]

sum1 = 0
for year in range(1901, 2001):
	day = 1
	day1 = 1
	first_date = [1]
	first_day = get_day_code(year)
	for i in range(1, 13):
		if i == 2:
			if get_leap_year(year):
				day = day + 29
				first_date.append(day)
			else:
				day = day + 28
				first_date.append(day)
		else:
			day = day + month[i]
			first_date.append(day)
	j = 1
	for i in first_date:
		if j == 13:
			break
		#if i==1 and first_day==0:
		#	sum1 = sum1+1
		day1 = day1+28
		if ((i-day1)+first_day)%7 == 0:
			sum1 = sum1+1
		#print j,"=",((i-day1)+first_day)%7,
		j = j+1
	#print first_date, sum1
print sum1
print memory_usage()