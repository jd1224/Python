

def pig_latin(word):
	firstL = word[0]
	vowels = 'aeiou'
	if firstL in vowels:
		return word+'ay'
	else:
		return word[1:]+firstL+'ay'
		
print(pig_latin('word'))
print(pig_latin('cork'))
print(pig_latin('air'))
print(pig_latin('apple'))