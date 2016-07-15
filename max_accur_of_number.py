
def max_accures(a):
	n = len(a)
	max = 0
	count = 1
	for i in range(n-1):
		for j in range(i+1, n):
			if a[i]==a[j]:
				count += 1
		if count > max:
			max = count
			count = 1
	
	return max

def reduce_complexity(a):
	#a = sort(a)
	n  = len(a)
	max = 0
	count = 1
	for i in range(n):
		if a[i] == a[i+1]:
			count = count + 1
		else:
			max = count 
			count = 1
	return max

a = [1,2,3,12,1,4,2,1,2,1,321,123,1]

v = max_accures(a)
print v

sort(a)
v1 = reduce_complexity(a)

print v1
