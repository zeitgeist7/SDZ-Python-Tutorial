#!/usr/local/bin/python3

a, b = 1, 2

print ("a = ", a)
print ("b = ", b)

# let's play with some strings
str = "Shut up!\n"
print(str * 2)

# some conditionals
print("Hello ")
inputValue =int(input("please enter a number :"))

if inputValue < 10 :
    print ("number is less than 10")
elif inputValue ==  10 :
    print ("number is exactly 10")
else :
    print ("number is greater than 10")

# iteration and looping
sentinel = 0;
while sentinel <= 1000 :
    print (sentinel)
    sentinel += 1 

print ("Entrees des donnees (Entrez vide pour terminer)")
sentinel = True
while sentinel :
    data = input()
    if data == "":
        sentinel = False
    else :
        print ("You have entered: ", data)

print("Enter some data (hit return when done)")
while True :
	data = input()
	if data ==  "" :
		print ("Thank you")
		break
	else :
		print("You have entered: ", data)

# Iterating through lists et al.
fruits = ['goyaves', 'mangue', 'poire', 'prunes']
for fruit in fruits :
	print("J'adore manger: ", fruit)

# Using range()
'''
    range(#) is a convenience 
    pre-version 3.x, range used to return a list, but now not anymore (type is I think range)
'''
for i in range(10) :
	print("i = ", i)


