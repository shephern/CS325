#1. split into two halves by x-coordinate
#2. Recursively compute closest pair in each half
#3. Solve merge step based on above results
#4. Determine set of points whose x-coords lie in
#   range of [Xm - d, Xm + d] where Xm is middle
#   line and d is currently found min distance
#5. Order the points in ascending order of their
#   y-coords
#6. Compare each point p to only those whose y-coord
#   differs from p by at most d
#7. return overall min distance

import As1HelperFunctions
from math import sqrt
testing = True

p = As1HelperFunctions.getMyPoints()

sortByX = sorted(p, key=lambda x: x[1])

firstHalf = []
secHalf = []

for i in range(0, len(sortByX)/2):
	firstHalf.append(sortByX[i])

for i in range(len(sortByX)/2, len(sortByX)):
	secHalf.append(sortByX[i])

if(testing):
	print "sortByX:\n",sortByX
	print "firstHalf:\n",firstHalf
	print "secHalf:\n",secHalf

def DandC(coords):
	print "" #so it compiles
	#algorith here (this is actually hard)
	#if base case
	#	solve and return
	#else do stuff
	#	DandC(coords/2)

#As1HelperFunctions.createOutputFile(min_dist, pairs, 1)