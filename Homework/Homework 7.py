import turtle

def counterLettersInAString(someString):
    counts = {}
    for char in someString:
        if counts.get(char):
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

countLtr = (counterLettersInAString('aurhklghzxcaudrgvxcvdfhuihgawrhhkrengio98456%*^%$^$*^&@ahrghqhargkfhh43th4n'))

#print(countLtr )
#print(len(countLtr))

ks = list(countLtr.keys())
ks.sort()
print(ks)


#18
def drawBar(t, height, mxht_bdr):
    """ Get turtle t to draw one bar, of height. """
    t.left(90)
    t.penup()
    t.forward(mxht_bdr-10)
    t.pendown()
    t.write(str(height))
    t.penup()
    t.right(180)
    t.forward(mxht_bdr-10)
    t.pendown()
    t.left(90)
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def barChart(t, data, mxht_bdr):
    for item in data:
        print(item)
        drawBar(t, item, mxht_bdr)

def main():
    countLtr = (counterLettersInAString('aurhklghzxcaudrgvxcvdfhuihgawrhhkrengio98456%*^%$^$*^&@ahrghqhargkfhh43th4n'))
    ks = list(countLtr.keys())
    ks.sort()
    maxheight = max(countLtr.values())
    numbars = len(ks)
    print(maxheight, numbars)
    border = 10

    wn = turtle.Screen()
    wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    #barChart(tess, ks, maxheight+border)

main()
