
class Circle():
	
	pi = 3.14
	
	def __init__(self,radius=1):
		self.radius = radius
		
	
	def get_circumference(self):
		return self.radius*self.pi*2
		

	def __str__(self):
		# return f"A radius of {self.radius} with a circumference of {self.get_circumference()}"