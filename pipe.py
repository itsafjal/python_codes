#! /usr/bin/python

import subprocess

def runbash(cmd):
	p=subprocess.Popen(cmd, shell=True , stdout=subprocess.PIPE)
	out=p.stdout.read().strip()
	return out.split('\n')


def changename(oldname, newnamebase):
	temp=oldname.split('.')
	newname=newnamebase + "."+ temp[1]
	subprocess.call(["mv", oldname, newname])


def changeallname(oldnamebase, newnamebase):
	
	files=runbash("ls")
	for afile in files:
		if(afile.split('.')[0]==oldnamebase):
			changename(afile, newnamebase)


def main():
	changeallname("test1", "new")

if __name__=='__main__':
	main()
