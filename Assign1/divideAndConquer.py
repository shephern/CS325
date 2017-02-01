import As1HelperFunctions
from math import sqrt

sortByX = sorted(As1HelperFunctions.getMyPoints(), key=lambda x: x[0])
#shortestPoints = [];

def DandC(coords):
	#Base Case: less than 4 points in list
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
		#Compute separation line:
		if(len(coords)%2 == 0): #If even number of coordinates
			#Take 2 middle x values, find difference, divide by two, add to smallest x value
			midLine = ( float((coords[len(coords)/2][0] - \
						coords[(len(coords)/2)-1][0]) / 2) + \
						coords[(len(coords)/2)-1][0] )
		else: #else odd number of coordinates
			midLine = coords[(len(coords)/2)][0]

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

		#minDist = (firstHalfDistance if (firstHalfDistance <= secHalfDistance) else secHalfDistance)
		minDist = min(firstHalfDistance, secHalfDistance)

		#Check around separation line
		closePoints = []
		lineRange = [midLine-minDist, midLine+minDist]
		for i in range(0, len(coords)):
			if(coords[i][0] >= lineRange[0] and \
			coords[i][0] <= lineRange[1]): #if the point is within range
				closePoints.append(coords[i])

		#if nothing to compare, return
		if (len(closePoints) < 2):
			return minDist

		#Split list into two halves
		midLinefirstHalf = []
		midLinesecHalf = []
		for i in range(0, len(closePoints)/2):
			midLinefirstHalf.append(closePoints[i])
		for i in range(len(closePoints)/2, len(closePoints)):
			midLinesecHalf.append(closePoints[i])

		#More Recursion!
		midLinefirstHalfDistance = DandC(midLinefirstHalf)
		midLinesecHalfDistance = DandC(midLinesecHalf)

		#otherMinDist = (firstHalfDistance if (firstHalfDistance <= secHalfDistance) else secHalfDistance)
		midLineMinDist = min(midLinefirstHalfDistance, midLinesecHalfDistance)

		return min(minDist, midLineMinDist)

shortestDistance = DandC(sortByX)
print shortestDistance
#As1HelperFunctions.createOutputFile(shortestDistance, pairs, 1)