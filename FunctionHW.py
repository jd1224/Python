import math

def volume(rad):
	t = rad**3
	q = 4/3
	return q*math.pi*t

	
def ran_check(num, low, high):
	return num>low and num<high
	
def up_low(s):
	up = 0
	low = 0
	for i in s:
		if i.isupper():
			up +=1
		elif i.islower():
			low +=1
	
		#print (i.isupper())
	print ("Number of uppercase letters is {}".format(up))
	print ("Number of lowercase letters is {}".format(low))
	

def unique_list(mylist):
	return list(set(mylist))
	
	
def multiply(nums):
	out = nums[0]
	for i in range(1,len(nums)):
		out *= nums[i]
	return out
	
def palindrome(word):
	return word == word[::-1]
	
def pangram(input):
	letters = list('abcdefghijklmnopqrstuvwxyz')
	for letter in input:
		if letter in letters:
			letters.remove(letter)
	return len(letters)==0
	
print (volume(2))
print (ran_check(5,2,7))
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print (unique_list([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,]))
print (multiply([1,2,3,-4]))
print (palindrome('hahah'))
print (pangram('The quick brown fox jumps over the lazy dog'))