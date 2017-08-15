#! python3

# KMP - Keynote Management Program

# The purpose of this program is to create and manage Revit keynotes on
# a project-by-project basis.

import os, sys, shutil, shelve

class Category():
	# Keynote category
	pass

class SubCategory():
	# Keynote subcategory
	pass


def openCreate ():
	# Opens or creates keynote file
	keyNoteFile = open(str(input('Enter Keynote File: ')), 'w+')
	return(keyNoteFile)
	# Choose to locate existing file to edit
	# Create new file

def writeKeynotes (keysfile):
	#Write or update changes to file
	keysfile.write('TEST')
	keysfile.close()

def categoryEdit ():
	# Create or edit keynote hierarchy
	pass

keysfile = openCreate()
writeKeynotes(keysfile)
