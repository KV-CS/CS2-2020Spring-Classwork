#1/14/2020

myString = "I do not fear computers. 67 I fear lack of them."

#Practice with some string methods
print(myString.lower())
print(myString.upper())
print(myString.capitalize())
print(myString.rfind('67'))

#Print each char out one at a time
for char in myString:
   print(char)

#Using format and length methods
print("My string is {} characters long".format(len(myString)))

#Check indicing
if myString[5] == 'n':
   print('Yes!')

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, {}! Your age is {}.".format(name, age))

