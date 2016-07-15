#! /usr/bin/python


def sum_two_element(a,k):

	n = len(a)
	i = 0
	j = n-1
	while(i!=j):
		if a[i] + a[j]==k:
			print i, j
			break
		elif a[i] + a[j] > k :
			j = j - 1
		else:
			i = i + 1


a = [1,2,5,4,63,2,3,4,7]

a.sort()

sum_two_element(a,7)
