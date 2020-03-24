# Darren Kong
# 110770716
# AMS326 Midterm 1

import math

def f(x):
    return 1/(1+25*math.pow(x,2))

def RundgeArea(n):
    trapArea = 0
    a1 = 0
    b1 = n
    while b1 <= math.sqrt(2):
        # uses trapazoidal rule
        trapArea += ((f(a1) + f(b1))/2)*(b1-a1)
        a1 += n
        b1 += n
    trapArea = 2*trapArea
    trapArea -= (1/26)*2
    return trapArea
def TriangleArea(b):
    return (25/26)*b*.5

def triangleLine(x,b):
    return (-(25/26)/b)*x + 1

def intersectionTest(x1, x2, b, increments, epsilon):
    interectionctr = 0
    while x1 <= x2:
        x1 += increments
        if abs(triangleLine(x1, b) - f(x1)) <= epsilon:
            interectionctr += 1
        if interectionctr > 1:
            return interectionctr
    return interectionctr
def findmaxbase(mins, maxs, increments, epsilon):
    b = increments
    while abs(maxs) - abs(mins) >= epsilon:
        b = (maxs + mins)/2
        if intersectionTest(0, .5, b, increments, epsilon) == 1:
            return b
        if intersectionTest(0, .5, b, increments, epsilon) < 1:
            mins = b+increments
        if intersectionTest(0, .5, b, increments, epsilon) > 1:
            maxs = b-increments
        #print(b)
    return b
RundgeArea = RundgeArea(math.pow(10, -5))
print("Area of enclosed Rundge function is " + str(RundgeArea))
base = findmaxbase(0, .4, math.pow(10, -5), math.pow(10, -5))
triArea = TriangleArea(2*base)
print("Base of the triangle is " + str(base))
print("Area of the triangle is " + str(triArea))

print("Remaining Area after cutting Traingle from Rundge function is " + str(RundgeArea-triArea))
