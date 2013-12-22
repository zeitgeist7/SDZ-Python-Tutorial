#!/usr/local/bin/py

# Open and write to a file
fichier = open("./testfile.txt", "w")
fichier.write("This is a day that I have been looking forward to for two and a half years.\n")
fichier.close()

# Open the file and append some contents to it
fichier = open("testfile.txt", "a")
fichier.write("Every once in a while, a revolutionary product comes along that changes everything.\n")
fichier.close()

# Use a for loop to write the line numbers in the file (boring)
fichier1 = open("colle.txt", "w")
for index in range(100) :
		fichier1.write("Line number " + str(index + 1) + ".\n")
fichier1.close()

# Write a list to a file
fruitList = ['oranges\n', 'goyaves\n', 'goyaves de chine\n', 'abricot\n', 'jamblons\n', 'papayes\n']
fruits = open("./fruits.txt", "w")
fruits.writelines(fruitList)
fruits.close()

# Read the bloody file
someFruits = open("fruits.txt", 'r')
for line in someFruits :
		print (line)
someFruits.close()
