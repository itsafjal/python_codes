#! /usr/bin/python


#enumerate is used when we need to iterate value and index both at same time

print("below listing with start index = 0")
a = [1,2,3,4,5,6]

for index, value in enumerate(a):
	print(index, value)



#we can also change the starting index

print("below listing with start index = 1")

for index, vlaue in enumerate(a, start = 1):
	print(index, value)
