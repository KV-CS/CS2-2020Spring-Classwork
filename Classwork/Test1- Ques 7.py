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

    storedWords = {}
    for item in data:
      storedWords[item]=len(item)

    largestLength = 0
    largestKey = ''

    for k , v in storedWords.items():
        if v > largestLength:
            largestKey = k
            largestLength = v

    print(largestKey, largestLength)

    #for item in storedWords:
     #   if storedWords[item] > storedWords[largest]:
      #      largest = item
            #print(largest)
    return largestKey

print(findLargestWord('../test_string_assessment1_CS2.txt'))
