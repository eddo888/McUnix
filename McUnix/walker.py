#!/usr/bin/env python3


import os, fnmatch


def listFiles(root, patterns='*', recurse=1, return_folders=0):

	# Expand patterns from semicolon-separated string to list
	pattern_list = patterns.split(';')

	class Bunch:
		'''
		Collect input and output arguments into one bunch
		'''

		def __init__(self, **kwds):
			self.__dict__.update(kwds)

	arg = Bunch(
		recurse=recurse,
		pattern_list=pattern_list,
		return_folders=return_folders,
		results=[])

	def visit(arg, dirname, files):
		# Append to arg.results all relevant files (and perhaps folders)
		for name in files:
			fullname = os.path.normpath(os.path.join(dirname, name))
			if arg.return_folders or os.path.isfile(fullname):
				for pattern in arg.pattern_list:
					if fnmatch.fnmatch(name, pattern):
						arg.results.append(fullname)
						break
			if os.path.islink(fullname):
				os.walk(fullname, visit, arg)
		# Block recursion if recursion was disallowed
		if not arg.recurse: files[:] = []

	os.walk(root, visit, arg)

	return arg.results

