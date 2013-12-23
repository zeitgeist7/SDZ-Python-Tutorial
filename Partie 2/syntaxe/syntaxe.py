#!/usr/local/bin/py

#	Creation of a syntaxe
#	Author: @zeitgeist7
#	Date of creation: 23 December 2013
#	Machine: MacBook Air

# Used for verifying existence of a file
import os

print ("**********************************\n" +
       "*     Simple syntax example      *\n" +
       "**********************************")

# Prompt user for project name
#projectName = input('Please provide a name for your project: ')

# Prompt user for sample file to use
sampleFileName = input('Please provide the name for the sample file to use: ')

while not os.path.exists(sampleFileName) :
		print('The sample file name that you provided does not exist.')
		sampleFileName = input('Please provide the name for the sample file to use: ')

# Open and read the sample file
sampleFile = open(sampleFileName, 'r')

# Parse sample file
for line in sampleFile :
		# Remove the newline caracter
		line = line.replace("\n", "")
		
		# Remove comment(s)
		line = line.split('#')[0]
		if line != '' :
				print(line)

