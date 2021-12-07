import re
inputfile = open("input10.txt", "r")
inputfile.readline()
inputfile.readline()
nodecount = int(inputfile.readline())
inputfile.readline()
nodeliststr=[]
nodeandpos=[]
for i in range(nodecount):
    nodeliststr.append(inputfile.readline())

for i in range(nodecount):
    nodeandpos.append(re.findall(r"[-+]?\d*\.\d+|\d+",nodeliststr[0]))