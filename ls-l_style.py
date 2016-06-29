#! /usr/bin/python

import subprocess

cmd1 = "echo you have these directory"

cmd2 = "ls -l"

cmd = [cmd1, cmd2]

for i in cmd:
	subprocess.call(i , shell=True)
