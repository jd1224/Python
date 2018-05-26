import math
class Line:
	
	def __init__(self,coord1,coord2):
		
		self.coord1 = coord1
		self.coord2 = coord2
		
	
	def __str__(self):
		return "coordinate1: "+str(self.coord1)+"\ncoordinate2: "+str(self.coord2)
		
		
	def slope(self):
		return (self.coord2[1]-self.coord1[1])/(self.coord2[0]-self.coord1[0])
		
	def distance(self):
		return math.sqrt(((self.coord2[0]-self.coord1[0])**2)+((self.coord2[1]-self.coord1[1])**2))
		
class Cylinder:

	
	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius
		
	def volume(self):
		pi = 3.14
		return pi*(self.radius**2)*self.height
	def surface_area(self):
		pi = 3.14
		
		return(2*(pi*self.radius**2))+((2*pi*self.radius)*self.height)