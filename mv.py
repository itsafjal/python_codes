#! /usr/bin/python

import subprocess

def changename(oldname, newbase):
	
	temp = oldname.split('.')
	newname= newbase+ "." + temp[1] + "." + temp[2]

	subprocess.call(["mv" , oldname , newname])

def main():
	oldname = "hello.1.txt"
	newbase= "go"
	changename(oldname , newbase)

if __name__ == '__main__':
	main()
