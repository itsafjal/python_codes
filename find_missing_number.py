


def missing(a):
	n = len(a)
	for i in range(n):
		if i not in a:
			print i



def sum_method(a):
	s1 = sum(a)
	n = len(a)
	s2 = int(((n)*(n+1))/2)
	print s2 - s1

def xor_method(a):
	x= a[0]^a[1]
	y = 0^1
	for i in range(2,len(a)):
		x = x^a[i]
	for i in range(2,len(a)+1):
		y = y^i
	print x^y

a = [0,3,2,4,6,1]

missing(a)

sum_method(a)

xor_method(a)
