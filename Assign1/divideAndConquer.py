#1. split into two halves by x-coordinate
#2. Recursively compute closets pair in each half
#3. Solve merge step based on above results
#4. Determine set of points whose x-coords lie in
#   range of [Xm - d, Xm + d] where Xm is middle
#   line and d is currently found min distance
#5. Order the points in ascending order of their
#   y-coords
#6. Compare each point p to only those whose y-coord
#   differs from p by at most d
#7. return overall min distance

