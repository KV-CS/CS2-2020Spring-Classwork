# "in"" and "not in" example, they function just how they sound
# "Accumulator" is building a string one char at a time.
# In other words, the string accumulates characters.
# The beenfit is you can make specific choices char by char.

def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels = sWithoutVowels + eachChar
    return sWithoutVowels


someString = ' iauhefihawihefaefr2353fbfbdjvb4389yrahjnzf'

print(removeVowels(someString))
