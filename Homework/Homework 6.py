#Homework 6
import turtle

file = open('labdata.txt', 'r')
line = file.readline()

rawList = []
while line:
    rawList.append(line.split())
    line = file.readline()

print('The raw list:', rawList)

#Create list of just X values
xList = []
yList = []
for item in rawList:
    xList.append(int(item[0]))
    yList.append(int(item[1]))

print(xList)
print(yList)


#Create averages of X and Y lists
avgX = sum(xList) / len(xList)
avgY = sum(yList) / len(yList)

print('avgX:', avgX, 'avgY:', avgY)


#Create combined XY list
combinedXY = []
for i in range(len(xList)):
    combinedXY.append([xList[i], yList[i]])
print(combinedXY)

maxX = max(xList)
maxY = max(yList)

don = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(0,0,maxX+10,maxY+10)

don.penup()

for point in combinedXY:
    don.goto(point[0], point[1])
    don.dot()

wn.exitonclick()
