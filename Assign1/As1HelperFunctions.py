import sys
inputFile = sys.argv[-1]

if (len(sys.argv) != 2):
	print "USAGE: python algorithm.py file.txt"
	exit();

with open(inputFile) as f:
	content = f.readlines()
content = [x.strip() for x in content]

myPoints = []
point = ();

for i in range(0, len(content)):
	myPoints.append([int(content[i][0]), int(content[i][2])])

print myPoints

def getMyPoints():
	return myPoints

def createOutputFile(minDistance, myPoints):
	outFile = open("output.txt", "w")
	outFile.write(str(minDistance)+"\n")
	outFile.write("\n".join(map(lambda x: str(x), myPoints)))
	outFile.write("\n")
	outFile.close()