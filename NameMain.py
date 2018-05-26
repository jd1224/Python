
def func():
	print("func in nameMain")

print ('top level in nameMain')

if __name__ == "__main__":
	print("NameMain is being run directly")
	
else:
	print("NameMain is imported")