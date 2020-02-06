# Homework 2
# Complete exercises 3, 11, 12 and 18.

#Exercise 3
# Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text - perhaps a
# poem, a speech, instructions to bake a cake, some inspirational verses, etc.
# Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text and then
# keeps track of how many are the letter ‘e’.

def alphNum(someText):
    numOfAlpha = 0
    countE = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for ch in someText:
        if ch in alpha or ch in alpha.upper():
            numOfAlpha += 1
        if ch == 'e' or ch == 'E':
            countE += 1
    return numOfAlpha, countE

quote = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cras pulvinar mattis nunc sed blandit libero volutpat sed cras. Tempus egestas sed sed risus pretium quam vulputate. Augue mauris augue neque gravida in fermentum et sollicitudin. Enim nunc faucibus a pellentesque. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet. Elit ut aliquam purus sit amet. Facilisis gravida neque convallis a cras semper auctor. Elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi. Felis bibendum ut tristique et egestas quis. Ac orci phasellus egestas tellus. Ac turpis egestas integer eget aliquet.

Tortor pretium viverra suspendisse potenti nullam ac. Rhoncus aenean vel elit scelerisque mauris pellentesque. Etiam non quam lacus suspendisse faucibus interdum posuere. Vel quam elementum pulvinar etiam non quam lacus suspendisse. Mi eget mauris pharetra et ultrices neque ornare aenean. Dignissim convallis aenean et tortor at risus viverra. Amet consectetur adipiscing elit duis. Amet commodo nulla facilisi nullam vehicula ipsum a arcu. Enim diam vulputate ut pharetra sit amet aliquam. Bibendum neque egestas congue quisque. Cras sed felis eget velit aliquet sagittis. Fringilla urna porttitor rhoncus dolor purus non enim praesent elementum. Velit egestas dui id ornare. Varius vel pharetra vel turpis nunc eget lorem dolor. Malesuada bibendum arcu vitae elementum curabitur vitae nunc. Purus sit amet volutpat consequat mauris nunc congue.

Aliquet sagittis id consectetur purus ut. Aliquam vestibulum morbi blandit cursus risus at ultrices. Parturient montes nascetur ridiculus mus mauris vitae ultricies leo integer. Posuere sollicitudin aliquam ultrices sagittis orci. Sed enim ut sem viverra aliquet. Habitasse platea dictumst quisque sagittis purus sit amet. Orci ac auctor augue mauris augue neque gravida in fermentum. Eget felis eget nunc lobortis mattis aliquam faucibus purus. Mi ipsum faucibus vitae aliquet. Tristique senectus et netus et malesuada fames ac. Etiam tempor orci eu lobortis elementum nibh tellus.

Fames ac turpis egestas maecenas pharetra convallis. Montes nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Mauris ultrices eros in cursus. Neque ornare aenean euismod elementum nisi quis eleifend quam adipiscing. Pharetra massa massa ultricies mi quis. Lectus arcu bibendum at varius vel pharetra vel turpis nunc. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae. Ornare massa eget egestas purus viverra accumsan in nisl. Semper feugiat nibh sed pulvinar proin gravida hendrerit. Neque ornare aenean euismod elementum nisi quis.

Quis viverra nibh cras pulvinar mattis. Sem et tortor consequat id porta. Bibendum ut tristique et egestas quis ipsum suspendisse ultrices. Velit dignissim sodales ut eu sem integer. Lacus vestibulum sed arcu non odio. Sodales ut etiam sit amet nisl purus. Viverra mauris in aliquam sem fringilla ut morbi tincidunt augue. Sagittis orci a scelerisque purus semper eget duis. Ultricies integer quis auctor elit sed. Mauris pellentesque pulvinar pellentesque habitant morbi. Odio eu feugiat pretium nibh ipsum. Nulla facilisi cras fermentum odio eu feugiat. Sollicitudin aliquam ultrices sagittis orci a. Senectus et netus et malesuada fames ac turpis egestas. Dictum fusce ut placerat orci nulla pellentesque dignissim enim sit. Id velit ut tortor pretium viverra suspendisse potenti.'''

#3 Tests
totalAlphaChars, countE = alphNum(quote)
percentE = countE / len(quote) * 100
print("Your text contains {} alphabetic characters, of which {} ({:.1f}%) are the lettter 'e'.".format(totalAlphaChars, countE, percentE))



# 11
# Write a function that removes the first occurrence of a string from another string.
def removeFromString(origString, strToRemove):
    location = origString.find(strToRemove)
    if location == -1:
        print('String not found')
        return origString
    newStr = origString[:location] + origString[len(strToRemove)+location:]
    return newStr

# 11 Tests
a='Kyle is the CS teacher Kyle Kyle Kyle'
b='CS'
print(removeFromString(a,b))

#12
# Write a function that removes all occurrences of a string from another string.
def replaceAllStrings(origString, strToReplace):
    newString = origString.replace(strToReplace, "")
    return newString

#12 Tests
print(replaceAllStrings(a, 'Kyle'))

#18
# Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted for another
# to garble the message. For example A -> Q, B -> T, C -> G etc. your function should take two parameters, the message
# you want to encrypt, and a string that represents the mapping of the 26 letters in the alphabet. Your function should
# return a string that is the encrypted version of the message.

def encryptMsg(unEncryptedString, key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    encryptedString = ''
    for ch in unEncryptedString:
        if ch == ' ':
            encryptedString = encryptedString + ' ' #adds spaces to encrypted msg
        else:
            index = alpha.find(ch.lower()) #Returns the index in the string where ch is found
            if index >= 0:
                encryptedString = encryptedString + key[index] #Uses index from alphabet as index for key
    return encryptedString

#18 Tests
key = 'qwertyuiopasdfghjklzxcvbnm'
myString = 'What are we going to do with this message'
print(encryptMsg(myString, key))
