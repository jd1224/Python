
#print ("Hello World!")

#sets are unordered colections of unique items
mySet = set()

mySet.add(1)

mySet.add(5)

mySet.add(2)

print (mySet)

#this will simply not be added, no exception is thrown
mySet.add(2)

#casting a list to a set will delete duplicates
myList = [1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,7,7,7,]

mySet1 = set(myList)

print (mySet1)


