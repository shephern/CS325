import As1HelperFunctions
from math import sqrt

sortByX = sorted(As1HelperFunctions.getMyPoints(), key=lambda x: x[0]) #O(n)

def DandC(coords):
	#returns [shortestDistance, [ ((point1x,point1y),(point2x,point2y)), ((point3x,point3y), (point4x,point4y)) ]]
	#assuming the distance between point1,point2 is the same as point3,point4

	#Base Case: less than 4 points in list
	#Find distance
	#Recurse back, compare recursed distances
	#Check points outside dividing line by min distance
	#Recurse back, etc.

	if(len(coords) <= 1): #Error
		return -1;
	elif(len(coords) == 2): #Base case
		#pythagorean theorem to find distance
		dist = sqrt(pow(coords[1][0]-coords[0][0], 2) + pow(coords[1][1]-coords[0][1], 2))
		return [dist, [(coords[0], coords[1])]]

	elif(len(coords) == 3): #Base case for odd numbers
		dist1 = sqrt(pow(coords[1][0]-coords[0][0], 2) + pow(coords[1][1]-coords[0][1], 2)) #0, 1
		dist2 = sqrt(pow(coords[2][0]-coords[1][0], 2) + pow(coords[2][1]-coords[1][1], 2)) #1, 2
		dist3 = sqrt(pow(coords[2][0]-coords[0][0], 2) + pow(coords[2][1]-coords[0][1], 2)) #0, 2

		if(dist1 <= dist2 and dist1 <= dist3):
			if(dist1 == dist2):
				if(dist1 == dist3):
					return [dist1, [(coords[0],coords[1]),(coords[0],coords[2]), (coords[1],coords[2])]]

				else:
					return [dist1, [(coords[0],coords[1]), (coords[1], coords[2])]]

			elif(dist1 == dist3):
				return [dist1, [(coords[0], coords[1]), (coords[0], coords[2])]]

			return [dist1, [(coords[0], coords[1])]]

		elif(dist2 < dist1 and dist2 <= dist3):
			if(dist2 == dist3):
				return [dist2, [(coords[0], coords[2]), (coords[1], coords[2])]]

			return [dist2, [(coords[1], coords[2])]]

		else:
			return [dist3, [(coords[0], coords[2])]]

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
		for i in range(0, len(coords)/2):
			firstHalf.append(coords[i])
		for i in range(len(coords)/2, len(coords)):
			secHalf.append(coords[i])

		#Recurse
		firstHalfDistance = DandC(firstHalf)
		secHalfDistance = DandC(secHalf)
		if(firstHalfDistance[0] == secHalfDistance[0]):
			minDist = [firstHalfDistance[0],[]]
			for i in range(0, len(firstHalfDistance[1])):
				minDist[1].append(firstHalfDistance[1][i])
			for i in range(0, len(secHalfDistance[1])):
				minDist[1].append(secHalfDistance[1][i])
		else:
			#True computer scientists use ternary operators
			minDist = firstHalfDistance if (firstHalfDistance[0] < secHalfDistance[0]) else secHalfDistance

		#Check around separation line
		closePoints = []
		lineRange = [midLine-minDist[0], midLine+minDist[0]]
		for i in range(0, len(coords)):
			if(coords[i][0] >= lineRange[0] and \
			coords[i][0] <= lineRange[1]): #if the point is within range
				closePoints.append(coords[i])

		#if nothing to compare, return
		if (len(closePoints) < 2):
			return minDist

		for i in range(0, len(closePoints)):
			for j in range(i+1, len(closePoints)):
				y = abs(closePoints[j][1] - closePoints[i][1])
				x = abs(closePoints[j][0] - closePoints[i][0])

				d = sqrt((y*y) + (x*x))
				if(d < minDist[0]):
					minDist = [d, [(closePoints[i],closePoints[j])]]
				elif(d == minDist[0]):
					minDist[1].append((closePoints[i],closePoints[j]))

		return minDist

answer = DandC(sortByX)
shortestDistance = answer[0]
pairs = list(set(answer[1]))
As1HelperFunctions.createOutputFile(shortestDistance, pairs, 1)