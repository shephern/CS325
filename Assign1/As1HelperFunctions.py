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

def getMyPoints():
	return myPoints

#minDistance ==> float of min distance
#myPoints ==> List of points with smallest interval
#AlgFlag ==> Int to determine name of output file
def createOutputFile(minDistance, myPoints, AlgFlag):

	if(AlgFlag == 0):
		outFile = open("output_bruteforce.txt", "w")
	else if(AlgFlag == 1):
		outFile = open("output_divideandconquer.txt", "w")
	else if(AlgFlag ==2):
		outFile = open("output_enhanceddnc.txt", "w")
	else:
		print "Error creating output file, fix AlgFlag"

	outFile.write(str(minDistance)+"\n")
	outFile.write("\n".join(map(lambda x: str(x), myPoints)))
	outFile.write("\n")
	outFile.close()
