#!/usr/bin/env python3

import os, sys, re

sys.path.insert(0, '..')

from McUnix.walker import listFiles

for file in listFiles('..'):
	print(file)
	
