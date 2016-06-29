#! /bin/bash

read name

if [ ! -n  "$name" ]
then
	echo "please enter a string"
else
	echo " hello $name"
fi
