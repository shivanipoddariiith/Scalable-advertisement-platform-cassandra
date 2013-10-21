#!/usr/bin/env python
import os
import sys
if __name__ == '__main__':
	if len(sys.argv) < 1:
		print "Format: ./script"
		exit(1)
	os.chdir("../src")
	os.system("python query.py")


