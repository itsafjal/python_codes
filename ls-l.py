#! /usr/bin/bash

import subprocess

print(subprocess.call("ls -l", shell=True))
