
def add(num1,num2):
	return int(num1)+int(num2)

running = True

while running:

	num1 = input("gimme a number: ")
	num2 = input("gimme another number: ")
	
	try:
		result = add(num1,num2)
		running = False
		
	except:
		print("Try again")
		continue
	else:
		print(result)