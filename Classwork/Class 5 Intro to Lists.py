import random
#Create A list containing 100 random integers
# Hint: Use iteration, random, and append

myList = []

print(myList)

for x in range(100):
    num = random.randint(0,1000)
    myList.append(num)

#myList.sort()
#print(myList)

def average(someList):
    '''Find the avg value given a list of ints'''
    total = 0
    for i in someList:
        total = total + i
    avg = total / len(someList)
    return avg

def findMax(someList):
    '''Find the max value given a list of ints'''
    largestNum = someList[0]
    for item in someList:
        if item > largestNum:
            largestNum = item
    return largestNum



