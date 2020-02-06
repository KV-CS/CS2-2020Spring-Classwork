
#Exercise 8
def removeFromString (myString, charToRemove):
    newString = myString.replace(charToRemove, "")
    return myString

testString = "akjdbnfq3ef43545yrthawwe4yrtbaeeeeeeeekjdv q4y9 pwaefadfaep98eeeeee"

removeFromString(testString,"e")
removeFromString(testString,"5")
removeFromString(testString,"45")



#Exercise 22
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: ${:.2f}'.format(total))
        else:
            moreItems = False
    average = total / count
    print('Total items: {:.2f}'.format(count))
    print('Total ${:.2f}'.format(total))
    print('Average price per item: ${:.2f}'.format(average))

checkout()
