infile = open("studentdata.txt", "r")

masterList = []
aline = infile.readline()
while aline:
    items = aline.split()
    masterList.append(items)
    aline = infile.readline()

print(masterList)
print(masterList[0][0])
