#Questions 5-7

'''
5. Write a function called encrypt_6() to encrypt a message. Your function will work like a substitution
cipher but each character is replaced by the character 6 characters to its left in the alphabet. For example the
letter “g” becomes the letter “a”. If a letter is past the letter “g” then the counting wraps around to the
letter “z” again, so “b” becomes “v”, “d” becomes “x” and so on.
Hint: Whenever you talk about things wrapping around it’s a good idea to think of modulo arithmetic.
'''

def encrypt_6(msg):
    newMsg = ''
    chars = 'abcdefghijklmnopqrstuvwxyz'
    for letter in msg:
        index = (chars.find(letter) -  6) % len(chars)
        newMsg = newMsg + chars[index]
    return newMsg

print(encrypt_6('compsci'))

'''
6. Create a list containing 101 random integers between 0 and 1000 (use iteration, append, and the random module).
Write three functions: average, median and average_median_compare. Each function will take the list of random 
integers as a parameter. The average_median_compare function will return the string “average” if the average 
value is greatest, “median” if the median value is greatest and "equal" if they are the same. Test your function 
for accuracy using a list of known values and then run it with the list of random integers you created.
'''
import random
myList = []
for i in range(101):
    myList.append(random.randint(0,1000))

def average(myList):
    avg = sum(myList) / len(myList)
    return avg

print(average(myList))

def median(myList):
    myList.sort()
    middle  = len(myList) // 2
    return myList[middle]

print(median(myList))

def average_median_compare(avg, med):
    if avg == med:
        return 'Equal'
    if avg > med:
        return 'Average'
    if med > avg:
        return 'Median'

print(average_median_compare(average(myList), median(myList)))

'''
7. Using dictionaries write a function that finds the longest word in a text? How many characters does it have? 
Your program should be written so that you can use any .txt file to test it. Test your program with the 
“test_string_assessment1_CS2.txt” text file.
'''
import string

def removePunct(someString):
    newstring = ''
    for char in someString:
        if char not in string.punctuation:
            newstring += char
    return newstring

def findLargestWord(someFile):
    f = open(someFile, 'r')
    data = f.read()
    data = removePunct(data)
    data = data.split()
    #print(data)

    storedWords = {}
    for item in data:
      storedWords[item]=len(item)

    largest = (list(storedWords.keys())[0])

    for item in storedWords:
        if storedWords[item] > storedWords[largest]:
            largest = item
            print(largest)
    return largest
print(type(string.punctuation))
print(findLargestWord('test_string_assessment1_CS2.txt'))

