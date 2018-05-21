
class Dog():
	species='mammal'
	furry=True
	
	def __init__(self,breed='Mutt',name='Unknown'):
		self.breed = breed
		self.name = name
	
	def speak(self):
		print ("I'm a dog, I say Woof.  My name is {}".format(self.name))

			
			


