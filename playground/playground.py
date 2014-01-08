'''
This file will be used as the playground for the tutorial
It will serve to test some newly learnt stuffs in the tutorial.
So far, Python seems a bit boring. But this tutorial seems promising.

Do not expect to be amazed if you have opened this file by curiousity!!!
'''

from Person import *

zeitgeist7 = Person('rajiv', 'jhoomuck', 'male', 'Jayantee')
print(zeitgeist7.parent)

'''
import string

def removePunctuations(punctuatedStr):
		punctuations = string.punctuation
		for punctuation in punctuations:
			punctuatedStr = punctuatedStr.replace(punctuation, "")
		return punctuatedStr

def palindromeHelper(str):
	if str.__len__() <= 1:
		return True
	elif str[0] == str[-1]:
		return isPalindrome(str[1:-1])
	print(str)
	return False

def isPalindrome(str):
	str = str.upper().replace(" ", "")
	# str = [character for character in str if character not in string.punctuation]
	str = removePunctuations(str)

	return palindromeHelper(str)


palindromes = ["civic", "Dewed", "deified", "dad", "mom", "devoved", "Hannah", "peeweep", "repaper", "kayak", "minim", "radar", "murdrum", "Malayalam", "madam", "lemel", "level", "racecar", "radar", "redder", "bob", "pop", "tot", "refer", "reviver", "rotator", "rotavator", "stats", "solos", "tenet", "terret", "testset", "Kinikinik", "Wassamassaw", "Yreka Bakery", "Navan", "Cain: a maniac.", "A Toyota.", "Race fast, safe car.", "A man, a plan, a canal: Panama.", "A dog, a plan, a canal: Pagoda.", "Desserts, I stressed!", "Drab as a fool, aloof as a bard.", "Live not on Evil.", "Madam, I'm Adam.", "Never odd or even.", "No lemon, no melon.", "Was it a car or a cat I saw?", "\"Not New York.\" Roy went on.", "Not so, Boston"]

# test(s)
for palindrome in palindromes:
	print(isPalindrome(palindrome))

'''



'''
def factorial(number) :
	"""
	Just a normal recursive function for the famous factorial function
	I have no idea whether that is very efficient since in JS it is not recommended to use recusion
	number : number whose factorial is to be calculated
	return : number!
	"""
	if number <= 1:
		return 1
	else :
		return number * factorial(number - 1)

print(factorial(100))
'''

'''
print((lambda number, power : number ** power)(2,4))
'''

'''
from funckyModule import *

printHello()
printWorld()
steveSaid()
'''

