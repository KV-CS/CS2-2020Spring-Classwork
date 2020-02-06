def applyRules(lhch):
    rhstr = ""
    if lhch == 'A':
        rhstr = 'B'   # Rule 1
    elif lhch == 'B':
        rhstr = 'C'  # Rule 2
    elif lhch == 'C':
        rhstr = 'BAC'
    else:
        rhstr = lhch    # no rules apply so keep the character
    return rhstr

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    #print(newstr)
    return newstr

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
        #print(startString)
    return endString

print(createLSystem(5, "A"))
