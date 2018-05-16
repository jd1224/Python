import re
#print ("Hello World!")

#creating a text file

myFile = open('myFile.txt')

#print (type(myFile))#show the type of the file

#print (myFile.read())#print the file to the console

myFile.seek(0)#reset the cursor to the zero position to re-read the file

#print (myFile.read())#print it to the console again

myFile1 = open("D:\\Program Files\\Notepad++\\Java\\ArrayListCluster.txt")# use and absolute path

#print (myFile1.read())#print the file

# best practice for opening a file is to place in a with loop

with open('myFile.txt') as myNewFile:
	contents = myNewFile.read()
	
	#print(contents)
	
myFile.close()
myFile1.close()


#file modes
#mode=r is read only
#mode=w is write only(will overwrite or create new files)
#mode=a is append only(adds to the end of the file)
#mode=r+ is read/write
#mode=w+ is writing and reading(overwrites or creates new files)

with open('myFile.txt',mode='r+') as myFile:
	contents = myFile.read()
	split = contents.split()
	i = 0
	regex = re.compile('.not.')
	for word in split:
		if (re.match(regex, word.lower())):
			i = i+1
	#print(contents)
	print (i)
	#myFile.write("\nChanged")
	#contents = myFile.read()
	#print(contents)

