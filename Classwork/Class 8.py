#Working with files

infile = open("qbdata.txt", "r")
outfile = open("qbnames.txt", "w")

#Reading with a for loop
for aline in infile:
    #print(type(aline))
    values = aline.split()
    #print(type(values))

    print('QB ', values[0], values[1], 'had a rating of ', values[10] )



infile = open("qbdata.txt", "r")
#Reading with a while loop
aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[1] + ',' + items[0]
    outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()
