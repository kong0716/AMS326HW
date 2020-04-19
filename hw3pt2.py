# Darren Kong
# 110770716
# AMS326

import math, random, numpy as np

tosses = 1984444444

def line_Intersects_Circle(a, b, c, x, y, r):
    # a, b, c given by the EQ of a line in a plane
    # x, y are the point coordinates / centerpoint of the circle
    # r is the radius of the circle
    dist = abs(x + c)

    if r > dist :
        return True
    return False

def genNCircleCenter(x, y, n):
    # x, y is the enclosing box where the center of the circle can be
    xlist = np.random.uniform(low=0, high=x, size=(n))
    #ylist = np.random.uniform(low=0, high=y, size=(n))
    return xlist

def buffon_Disc(xrange, yrange, nlines, d, tosses):
    line_eq = [0]
    x = 0
    while x <= xrange:
        x += xrange/nlines
        line_eq.append(x)
    # line_eq last item will always be bigger than x range
    line_eq = line_eq[:-1]
    #print(line_eq)
    radius = d/2
    intersects = 0
    xlist = genNCircleCenter(xrange, yrange, tosses)
    for i in range(tosses):
        #print(x, y)
        #flag = 0
        for l in line_eq:
            if line_Intersects_Circle(1, 0, -l, xlist[i], 0, radius):
                intersects += 1
                #flag += 1
                break
                #print(x ,y)
                #print(l)
                #if flag >= 2:
                #    print("Error")
        if i % 1000000 == 0:
            print(i)
    print(intersects/tosses)
import time
start_time = time.time()
buffon_Disc(10, 10, 10, .75, tosses)
#genNCircleCenter(10, 10, tosses)
print("--- %s seconds ---" % (time.time() - start_time))