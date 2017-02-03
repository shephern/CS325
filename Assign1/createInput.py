import sys
import random
import time

if (len(sys.argv) != 3):
    print "USAGE: python createInput.py fileName.input num"
    exit();

pfile = open(str(sys.argv[1]), "w")

points = []
random.seed(time.time())

for i in range(int(sys.argv[2])+1):
    #Point range may need to be changed for large sample sizes
    p = tuple(random.sample(range(-200,200),2))
    if p not in points:
        points.append(p)

for i in points:
    for val in i:
        pfile.write(str(val))
        pfile.write(" ")
    pfile.write("\n")
