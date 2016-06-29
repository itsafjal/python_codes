#! /usr/bin/python

import subprocess
import argparse
import re
parser = argparse.ArgumentParser(description="batch change filename")
parser.add_argument("inputfilename", metavar="basenamein")
parser.add_argument("outputfilename" , metavar="basenameout")
args=parser.parse_args()

def runbash(cmd):
	p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out=p.stdout.read.split()
	return out.split('\n')


def changename(oldname , newbase):
	temp=re.split('([0-9])', oldname)
	newname=newbase + "." + temp[1]
	subprocess.call("mv", oldname , newname)

def changeall(oldnamebase, newnamebase):
	files=runbash("ls")
	for afile in files:	
		temp=re.split('([0-9])', afile)
		if(temp[0] == oldnamebase):
			changename(oldnamebase, newnamebase)

changeall(args.inputfilename , args.outputfilename)
