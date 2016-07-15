#! /usr/bin/python


def swap(a):
	n = len(a)
	i = 0
	for i in range(1,int(n/2),i+2):
		temp = a[i]
		a[i] = a[int(n/2)+i-1]
		a[int(n/2)+i-1] = temp	
	return a

a = [1,2,3,4,5,6,7,8]

v = swap(a)

print v
