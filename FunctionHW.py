import math

def volume(rad):
	t = rad**3
	q = 4/3
	return q*math.pi*t
	
print (volume(2))