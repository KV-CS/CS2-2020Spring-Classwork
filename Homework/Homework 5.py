# Homework 5
import random

#Problem 4
myList = []
for i in range(100):
    myList.append(random.randint(0,1000))
print(myList)

def avg(someList):
    avg = sum(someList) / len(someList)
    return avg
print(avg(myList))

#Problem 6
def sum_of_sq(someList):
    for i in range(len(someList)):
        someList[i] = someList[i] * someList[i]
    return sum(someList)

print(sum_of_sq([2,3,4]))

#Problem 8
#Sum all the even numbers in a list
def sum_even_nums(someList):
    total = 0
    for num in someList:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_nums([2,3,4,5,6,7,8,9,10]))

#Problem 10
def length5(someList):
    count = 0
    for item in someList:
        if len(item) == 5:
            count += 1
    return count

print(length5(['hello', 'goody', 'wordy', 'smith', 'no', 'nope', 'yes?']))
