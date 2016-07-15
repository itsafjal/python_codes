

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b, a%b)


#a = list(map(int, input().split()))

#v1 = a[0]+a[1]
#v2 = a[2] + a[3]

v = gcd(2 ,8)

if v==1 or v==min(2,8):
	print("YES")
else:
	print("NO")
