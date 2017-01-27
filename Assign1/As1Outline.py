import sys
inputFile = sys.argv[-1]

with open(inputFile) as f:
	content = f.readlines()
content = [x.strip() for x in content]

myPoints = []
point = ();

for i in range(0, len(content)):
	myPoints.append([int(content[i][0]), int(content[i][2])])

print myPoints

#content = map(int, content);
