#! /usr/bin/env python
## from decimal import Decimal
a = 1
b = 1
c = 0
f = open("numbers.txt", "w+")
times = 0
while 1:
	times += 1
	c = a
	a = a+b
	b = c
	print "Numbers calculated: " + str(times)
	t = str(a) + "\n"
	f.write(t)
	
	'''
		Fibbonacci also can be used to get an aproximated
		value of phi number
		## print Decimal(a)/Decimal(c)
	'''