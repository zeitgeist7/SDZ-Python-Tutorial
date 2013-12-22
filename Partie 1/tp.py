#!/usr/local/bin/py

'''
The author does not want us to use functions at this moment,
so we will refrain from using...
'''
import random

# print the welcome text
print("\n*** Juste Prix ***\n")

# show options
print("Choix de la difficulté:")
print("1 : Entre 1 - 10")
print("2 : Entre 10 -100")
print("3 : Entre 100 - 1000")
print("4 : Entre 1000 - 10000")

# prompt for choice
choice = int(input("--> "))

# inform if bad choice
if 0 > choice and choice > 5 :
		print("You just made a bad choice, goodbye")

print("Le jeu commence, alors combien?")

leJustePrix = 0
minAmount, maxAmount = 0, 0

# actions based on the choices
if choice == 1:
		leJustePrix = random.randrange(1, 10)
elif choice == 2 :
		leJustePrix = random.randrange(10, 100)
elif choice == 3 :
		leJustePrix = random.randrange(100, 1000)
else : 
		leJustePrix = random.randrange(1000, 10000)

# Logging
print("\n\nLe juste prix est :", leJustePrix, "\n\n")

numberOfAnswers = 0
while True :
		answer = int(input())
		if answer == leJustePrix :
				print("Vous avez trouvez la solution avec ", numberOfAnswers, "essais.")
				break
		elif answer < leJustePrix :
				print("Plus!")
		elif answer > leJustePrix :
				print("Moins!")	
		
		numberOfAnswers += 1
