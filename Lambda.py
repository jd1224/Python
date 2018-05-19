
def square(num):
	return num**2
	
my_nums = [1,2,3,4,5]

i =(list(map(square,my_nums)))
print (i)
	
def check_even(num):
	return num%2 ==0
	
j = list(filter(lambda num:num%2==0, i))
print (j)

namesList = ['Andy', 'Eve', 'Sally']

print (list(map(lambda name: name[0], namesList)))






