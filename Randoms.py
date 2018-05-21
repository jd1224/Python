from random import shuffle
from random import randint
from random import choice

myList1 =[1,2,3,4,5,6,7,8,9]
myList2 = ['a','b','c']
myString = 'hello'

myList3 = [letter for letter in myString]


myDict = {}
for key,value in zip(myList1,myList2):
	myDict[key] = value

shuffle(myList1)

#x = int(input('Enter a Number: '))

print (myList3)
		
