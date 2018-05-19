
def lesser_of_two_evens(a,b):
	if a%2==0 and b%2==0:
		return min(a,b)
	else:
		return max(a,b)

def animal_crackers(text):
	splitUp = text.split()
	return splitUp[0][0].lower == splitUp[1][0].lower
	
def makes_twenty(x,y):
	return x+y==20 or x==20 or y==20
	
def old_macdonald(name):
	return name[:3].capitalize()+name[3:].capitalize()
	
def master_yoda(text):
	splitUp = text.split()
	splitUp.reverse()
	return " ".join(splitUp)
	
def almost_there(n):
	return (abs(100-n)<=10)or(abs(200-n)<=10)
	
def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i]==3 and nums[i+1]==3:
			return True

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
		if 11 in nums and sum<=31:
			sum = sum - 10
			return sum
		else:
			return 'BUST'
	else:
		return sum

def summer_of_69(nums):
	inside = False
	total = 0
	for i in nums:
		if i==6:
			inside = True
		if inside:
			if i==9:
				inside = False
			else:
				continue
		elif not inside:
			total += i
	return total
		
def spy_game(nums):
	code = [0,0,7,'x']
	
	for i in nums:
		if i == code[0]:
			code.pop(0)
	return len(code)==1

def count_primes(nums):
	if nums < 2:
		return 0
	prime = nums-2
	for i in range(0,nums):
		for j in range (2,i-1):
			if i%j==0:
				prime = prime -1
				break
	return prime

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
print ("\n")
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print ("\n")
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
print ("\n")
print(old_macdonald('macdonald'))
print ("\n")
print(master_yoda('I am home'))
print(master_yoda('We are ready'))
print ("\n")
print (almost_there(90))
print (almost_there(104))
print (almost_there(150))
print (almost_there(209))
print ("\n")
print (has_33([1,3,3]))
print (has_33([1,3,1,3]))
print (has_33([3,1,3]))
print ("\n")
print (paper_doll('hello'))
print (paper_doll('mississippi'))
print ("\n")
print (blackJack(5,6,7))
print (blackJack(9,9,9))
print (blackJack(9,9,11))
print ("\n")
print (summer_of_69([1,3,5]))
print (summer_of_69([4,5,6,7,8,9]))
print (summer_of_69([2,1,6,9,11]))
print ("\n")
print (spy_game([1,2,4,0,0,7,5]))
print (spy_game([1,0,2,4,0,5,7]))
print (spy_game([1,7,2,0,4,5,0]))
print ("\n")
print (count_primes(100))