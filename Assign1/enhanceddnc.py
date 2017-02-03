#1. Pre sort points based on x and y values
#2. Split points into two halves based on the x value
#3. Call function on each half
#4. Merge by pruning [Xm - d, Xm + d] where Xm is the median line
#   and d is the min of left and right side
#5. Return minimum distance, eliminating points that excede (p+-d,p+-d)

import As1HelperFunctions
import pprint as prn
from math import sqrt
testing = True

rawPoints = As1HelperFunctions.getMyPoints()
sortByX = sorted(rawPoints, key=lambda x: x[0])
sortByY = sorted(rawPoints, key=lambda y: y[1])

def enhanceddnc(xSorted, ySorted):
    #Base Case: less than 4 points in the list
    #Find distance
    #Recurse Back, compare recursed distances
    #Check points outside dividing line by min distance

    #This can be reduced to basecase 1 and 2 as if two points are minimum distance than
    #  combination wouldn't consider the third

    #Note: I used xSorted to calculate median and distance, though ySorted could've been used
    if(len(xSorted) <= 1): #Error
        return -1;
    elif(len(xSorted) == 2): #Base case
        #pythagoras
        dist = sqrt(pow(xSorted[1][0]-xSorted[0][0], 2) + pow(xSorted[1][1]-xSorted[0][1], 2))
        return [[(tuple(xSorted[0]),tuple(xSorted[1]))], dist]
    elif(len(xSorted) == 3): #Base case for odd numbers
        a = tuple(xSorted[0])
        b = tuple(xSorted[1])
        c = tuple(xSorted[2])
        abDist = sqrt(pow(xSorted[1][0]-xSorted[0][0], 2) + pow(xSorted[1][1]-xSorted[0][1], 2))
        acDist = sqrt(pow(xSorted[2][0]-xSorted[0][0], 2) + pow(xSorted[2][1]-xSorted[0][1], 2))
        bcDist = sqrt(pow(xSorted[2][0]-xSorted[1][0], 2) + pow(xSorted[2][1]-xSorted[1][1], 2))
        retPairs = []
        minDist = min([abDist, acDist, bcDist])
        if abDist == minDist:
            retPairs.append((a,b))
        if acDist == minDist:
            retPairs.append((a,c))
        if bcDist == minDist:
            retPairs.append((b,c))
        return [retPairs, minDist]
    else:
        #Compute seperation line
        if(len(xSorted)%2 == 0):   #Even number of points
            #Take 2 middle x values, find the mean
            midVal = float((xSorted[int(len(xSorted)/2)][0] +
                               xSorted[int((len(xSorted)/2)-1)][0])/ 2)
        else: #else odd number of points
            midVal = xSorted[int(len(xSorted)/2)][0]
        midInd = int(len(xSorted)/2)

        #Split the coordinates down the median, preserving x and y sorts
        leftXsorted = xSorted[:midInd]
        leftYsorted = []
        rightXsorted = xSorted[midInd:]
        rightYsorted = []


        i = 0
        while i < len(ySorted):
            if(ySorted[i] in leftXsorted):
                leftYsorted.append(ySorted[i])
            else:
                rightYsorted.append(ySorted[i])
            i = i + 1
        
        #Recursive step
        leftRet = enhanceddnc(leftXsorted,leftYsorted)
        rightRet = enhanceddnc(rightYsorted, rightYsorted)
        
        pairs = []
        #Combination step
        minDist = min(leftRet[1], rightRet[1])
        if leftRet[1] == minDist:
            pairs.extend(leftRet[0])
        if rightRet[1] == minDist:
            pairs.extend(rightRet[0])
        checkY = []
        
        i = 0
        #Go through all points, discarding those out of range
        while i < len(ySorted):
            if((ySorted[i][0] >= midVal - minDist) and (ySorted[i][0] <= midVal + minDist)):
                checkY.append(ySorted[i])
            i = i + 1
        #Check each point in x =[mid-d,mid+d] against those within d distance
        
        for p in range(0, len(checkY)-1):
            #For each point, check the points in checkY within d distance
            #At most, check the next seven points
            for q in range(p+1, p+8):
                if q > len(checkY) - 1:
                    #Exceeds bounds
                    break
                if checkY[q][1] - checkY[p][1] > minDist:
                    break #past maximum for minimum distance on y-axis
                else:
                    dist = sqrt(pow(checkY[p][0]-checkY[q][0], 2) + pow(checkY[p][1]-checkY[q][1], 2))
                    if dist < minDist:
                        #New minimum
                        pairs = [(tuple(checkY[p]),tuple(checkY[q]))]
                        minDist = dist
                    elif dist == minDist:
                        #New pair for same min
                        if((tuple(checkY[p]), tuple(checkY[q])) not in pairs):
                            pairs.append((tuple(checkY[p]), tuple(checkY[q])))
                    #Otherwise no change, minimum remains
        return [pairs, minDist]

# t0 = As1HelperFunctions.getTime()
answer = enhanceddnc(sortByX, sortByY)
# t1 = As1HelperFunctions.getTime()
# As1HelperFunctions.calcTime(t0,t1,0)

shortestDist = answer[1]
pairs = list(set(tuple(answer[0])))

As1HelperFunctions.createOutputFile(shortestDist, answer[0], 2)
