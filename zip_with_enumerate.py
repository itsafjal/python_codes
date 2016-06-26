#! /usr/bin/python


a = [1,2,3,4,5,6]

b = [2,3,4,5,6,7]

# zip is used to iterate over two lists at same time 


for index, (a,b) in enumerate(zip(a,b)):

	print index, a , b


