f = open('alice-in-wonderland', 'r')
count = {}

for line in f:
    for word in line.split():
        #print(word)
        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = list(count.keys())
keys.sort()


# save the word count analysis to a file
out = open('alice_words.txt', 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')

wordLengthDist = {}
#print("The word 'alice' appears " + str(count['alice']) + " times in the book.")
for key in count:
    print(key)
    if key in wordLengthDist:
        wordLengthDist[count[key]] += 1
    else:
        wordLengthDist[count[key]] = 1

print(wordLengthDist)
keys = list(wordLengthDist.keys())
keys.sort()
print(keys[-5:])
