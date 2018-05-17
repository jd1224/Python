#discusses *args and **kwargs

def myFunction(*args):#takes an unlimited amount of args and stores as a tuple
	print (args)

def myFunction1(**kwargs):#takes key:value pairs and creates a dictionary
	print (kwargs)
	if 'fruit' in kwargs:
		print('the fruit is {}'.format(kwargs['fruit']))
	else:
		print('no fruit found sucka')
	
	
myFunction(1,2,3,4,5,6)

myFunction1(fruit='apple',veggie='lettuce')
myFunction1(bread='rye')