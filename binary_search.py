#! /usr/bin/python

def binary_search(a, k):

	low = 0
	high = len(a)-1
	n  = len(a)

	mid = low + int((high-low)/2)	
	while(low<=high):
	
		mid = low + int((high-low)/2)

		if a[mid] == k:
			return mid

		elif a[mid]<k:
		
			low = mid+1 
		else:
			high = mid - 1
	
	return -1

a = [3,34,345,432,444,555]

v = binary_search(a,30)

if v == -1:
	print "value not found"
else:
	print v
