
def lesser_of_two_evens(a,b):
	if a>b:
		greater = a
		lower = b
	else:
		greater = b
		lower = a
	if a%2==0 and b%2==0:
		return lower
	else:
		return greater




def animal_crackers(text):
	splitUp = text.split()
	if splitUp[0][0].lower == splitUp[1][0].lower:
		return True
	else:
		return False
	

def makes_twenty(x,y):
	if x==20 or y ==20:
		return True
	elif x+y==20:
		return True
	else:
		return False
	
	
def old_macdonald(name):
	return name[0].upper()+name[1:3]+name[3].upper()+name[4:]
	
	
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
	
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

print(old_macdonald('macdonald'))