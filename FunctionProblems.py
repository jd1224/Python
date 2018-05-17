
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
	
	
def master_yoda(text):
	splitUp = text.split()
	splitUp.reverse()
	return " ".join(splitUp)
	
	
def almost_there(n):
	if n>=90 and n<=110:
		return True
	elif n>=190 and n<=210:
		return True
	else:
		return False
	
	
def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i]==3 and nums[i+1]==3:
			return True
		else:
			continue
	return False
			
def paper_doll(text):
	outText = ''
	for i in text:
		outText = outText+i+i+i
		
	return outText

def blackJack(a,b,c):
	sum = a+b+c
	nums = [a,b,c]
	if sum>21:
		if 11 in nums:
			sum = sum - 10
			return sum
		else:
			return 'BUST'
	else:
		return sum
		
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
	
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

print(old_macdonald('macdonald'))

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print (almost_there(90))
print (almost_there(104))
print (almost_there(150))
print (almost_there(209))

print (has_33([1,3,3]))
print (has_33([1,3,1,3]))
print (has_33([3,1,3]))

print (paper_doll('hello'))
print (paper_doll('mississippi'))

print (blackJack(5,6,7))
print (blackJack(9,9,9))
print (blackJack(9,9,11))