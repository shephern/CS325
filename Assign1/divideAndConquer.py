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

# if(testing):

# 	print len([1,2,3,4,5])/2

# 	firstHalf = []
# 	secHalf = []
# 	for i in range(0, floor(len(sortByX)/2)):
# 		firstHalf.append(sortByX[i])
# 	for i in range(floor(len(sortByX)/2)), len(sortByX)):
# 		secHalf.append(sortByX[i])

# 	print "sortByX:\n",sortByX
# 	print "firstHalf:\n",firstHalf
# 	print "secHalf:\n",secHalf

def DandC(coords):
	#Base Case: Only two points in section
	#Find distance
	#Recurse back, compare recursed distances
	#Check points outside dividing line by min distance
	#Recurse back, etc.

	if(len(coords) <= 1): #Error
		return -1;
	elif(len(coords) == 2): #Base case
		#pythagorean theorem to find distance
		return sqrt(pow(coords[1][0]-coords[0][0], 2) + pow(coords[1][1]-coords[0][1], 2))
	elif(len(coords) == 3): #Base case for odd numbers
		return min(sqrt(pow(coords[1][0]-coords[0][0], 2) + pow(coords[1][1]-coords[0][1], 2)), \
				   sqrt(pow(coords[2][0]-coords[1][0], 2) + pow(coords[2][1]-coords[1][1], 2)), \
				   sqrt(pow(coords[2][0]-coords[0][0], 2) + pow(coords[2][1]-coords[0][1], 2)) )

	else:
		#Split list into two halves
		firstHalf = []
		secHalf = []
		for i in range(0, len(coords)/2): #Note: len(coords)/2 rounds down for odd numbers
			firstHalf.append(coords[i])
		for i in range(len(coords)/2, len(coords)):
			secHalf.append(coords[i])

		#Recurse
		firstHalfDistance = DandC(firstHalf)
		secHalfDistance = DandC(secHalf)
		if (firstHalfDistance <= secHalfDistance):
			minDist = firstHalfDistance
		else:
			minDist = secHalfDistance

		#minDist = (firstHalfDistance if (firstHalfDistance <= secHalfDistance) else secHalfDistance)

		return minDist
		#Check points around dividing line

shortestDistance = DandC(sortByX)
print shortestDistance

#As1HelperFunctions.createOutputFile(min_dist, pairs, 1)