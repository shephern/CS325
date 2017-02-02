import sys
inputFile = sys.argv[-1]

if (len(sys.argv) != 2):
	print "USAGE: python algorithm.py file.txt"
	exit();

##with open(inputFile) as f:
##	content = f.readlines()
##content = [x.strip() for x in content]
##
myPoints = []
##point = ();
##for i in range(0, len(content)):
##	myPoints.append([int(content[i][0]), int(content[i][2])])

# I was able to solve the double, multidigit problem with linesplit
with open(inputFile) as f:
        content = [word for line in f for word in line.split()]
i = 0
while i < len(content):
	myPoints.append((float(content[i]), float(content[i+1])))
	i = i + 2

def getMyPoints():
	return myPoints

#minDistance ==> float of min distance
#myPoints ==> List of points with smallest interval
#AlgFlag ==> Int to determine name of output file
def createOutputFile(minDistance, myPoints, AlgFlag):

	if(AlgFlag == 0):
		outFile = open("output_bruteforce.txt", "w")
	elif(AlgFlag == 1):
		outFile = open("output_divideandconquer.txt", "w")
	elif(AlgFlag ==2):
		outFile = open("output_enhanceddnc.txt", "w")
	else:
		print "Error creating output file, fix AlgFlag"

	outFile.write(str(minDistance)+"\n")
	myPoints.sort()
	for pair in myPoints:
                for coord in pair:
                        for val in coord:
                                outFile.write(str(val))
                                outFile.write(" ")
                outFile.write("\n")
	outFile.close()
