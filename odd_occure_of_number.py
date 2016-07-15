

def odd_occure(a):
	x = a[0]^a[1]
	for i in range(2,len(a)):
		x = x^a[i]

	print x


a = [1,2,2,2,1,3,3,1,2,2,2]


odd_occure(a)
