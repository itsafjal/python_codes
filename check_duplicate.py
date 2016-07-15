#! /usr/bin/python


a = [4,2,3,1,2,3,4,5]

n = len(a)

for i in range(n-1):
	for j in range(i+1, n):
		
		if a[i]==a[j]:
			print "element found"
			break

