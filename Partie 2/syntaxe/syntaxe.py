#!/usr/local/bin/py

#   Creation of a syntaxe
#   Author: @zeitgeist7
#   Date of creation: 23 December 2013
#   Machine: MacBook Air

# used for verifying existence of a file
import os

print ("**********************************\n" +
    "*     Simple syntax example      *\n" +
    "**********************************")

# prompt user for project name
projectName = input('Please provide a name for your project: ')

# Prompt user for sample file to use
sampleFileName = input('Please provide the name for the sample file to use: ')

while not os.path.exists(sampleFileName) :
    print('The sample file name that you provided does not exist.')
    sampleFileName = input('Please provide the name for the sample file to use: ')

# Open and parse the sample file

sampleFile = open(sampleFileName, 'r')
lineNumber = 1  # yeah, we could do that in another way
operations = []

for line in sampleFile :
    # remove the newline caracter
    line = line.replace("\n", "")
    
    # remove comment(s)
    line = line.split('#')[0]
    if line != '' :
        if lineNumber == 1 :
            # remove all the spaces
            line = line.replace(' ', '')
            # grab the operations
            operations = line.split(',')
            print(operations)
        elif lineNumber == 2 :
            # separate the numbers
            firstBatchOfNumbers = line.split(' ')
            # remove extra spaces
            while '' in firstBatchOfNumbers :
                firstBatchOfNumbers.remove('')
            print(firstBatchOfNumbers)

        elif lineNumber == 3 :
            # remove the brackets and the commas and separate the numbers
            secondBatchOfNumbers = line.replace(' ', '').replace('[', '').replace(']', '').split(',')
            print(secondBatchOfNumbers)

        lineNumber += 1

# We are done
sampleFile.close()

# Associate a name to each operation ans handle invalid operator encountered
for operation in operations :
    if operation == '+' :
        nomOperation = 'addition'
    elif operation == '-' :
        nomOperation = 'subtraction'    
    elif operation == '*' :
        nomOperation = 'multiplication' 
    elif operation == '/' :
        nomOperation = 'division'
    elif operation == '%' :
        nomOperation = 'modulo'
    elif operation == '**' :
        nomOperation = 'puissance'
    elif operation == '//' :
        nomOperation = 'divisionEntiere'
    else :
        print('The operation marked \'%s\' is not known.' %(operation))
        continue
    print('Generation des fichiers pour l\'operation %s' %(operation))
    # For each value
    for value in firstBatchOfNumbers :
        # Creation du fichier
        fichier = open("%s-%s-%s.txt" % (projectName, nomOperation, value), 'w')
        for nombre in range(eval(secondBatchOfNumbers[0]),eval(secondBatchOfNumbers[1]),eval(secondBatchOfNumbers[2])) :
            if (operation == '/' or operation == '//' or operation == '%') and nombre == 0 :
                fichier.write("%s %s %s = impossible !\n" % (value.center(10), operation, str(nombre).center(10))) 
            else :
                fichier.write("%s %s %s = %f\n" % (value.center(10), operation, str(nombre).center(10), eval(value+operation+str(nombre))))
        # Fermer le fichier :
        fichier.close()

