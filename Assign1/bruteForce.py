import As1HelperFunctions
from math import sqrt

p = As1HelperFunctions.getMyPoints()

coords = []
dists = []
for i in range(0, len(p)):
   for j in range(i+1, len(p)):
      y = abs(p[j][1] - p[i][1])
      x = abs(p[j][0] - p[i][0])

      d = sqrt((y*y) + (x*x))
      
      coords.append([p[i], p[j]])
      dists.append(d)

pairs = []
indices = [i for i, x in enumerate(dists) if x == min(dists)]
for z in range(0, len(indices)):
   #print indices[z]
   pairs.append(coords[indices[z]])

pairs.sort()
min_dist = min(dists)

As1HelperFunctions.createOutputFile(min_dist, pairs, 0)
