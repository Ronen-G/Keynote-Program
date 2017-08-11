#! python3

# KMP - Keynote Management Program

# The purpose of this program is to create and manage Revit keynotes on
# a project-by-project basis.

import os, sys, shutil


def openCreate ():
	# Opens or creates keynote file
	
	# Choose to locate existing file to edit
	# Create new file

def categoryEdit ():
	# Create or edit top most keynote hierarchy


keyNoteFile = open(str(input('Enter Keynote File: ')), 'r+')
KeyNoteFile.write('TEST')
KeyNoteFile.close()
