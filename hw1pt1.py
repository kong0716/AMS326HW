# Darren Kong
# 110770716
# AMS326HW1
# Problem1.1
import math
import random

# Functions taken from problem, creates a half heart together
def f_(x):
    # Bounds are from 0 to sqrt(2)
    return math.sqrt(2-math.pow(x,2)) + math.sqrt(x)

def h_(x):
    # Bounds are from 0 to sqrt(2)
    return -math.sqrt(2-math.pow(x,2)) + math.sqrt(x)
    
def trapazoidal_rule(n, a, b):
    trapArea = 0
    a1 = a
    b1 = a+n
    while b1 <= b:
        trapArea += ((f_(a1) + f_(b1))/2)*(b1-a1)
        a1 += n
        b1 += n
    return trapArea
#print(crude_montecarlo(100000000, 0, math.sqrt(2), 0, 2.1))
#print(trapazoidal_rule(.000001, 0, math.sqrt(2)))

def heartArea(n):
    # Area above the x-axis
    trapArea = 0
    a1 = 0
    b1 = n
    while b1 <= math.sqrt(2):
        # uses trapazoidal rule
        trapArea += ((f_(a1) + f_(b1))/2)*(b1-a1)
        a1 += n
        b1 += n
    a1 = 1
    b1 = 1 + n
    while b1 <= math.sqrt(2):
        #subtract since it is the area under the curve and we want to subtract that from previous area
        trapArea -= ((h_(a1) + h_(b1))/2)*(b1-a1)
        a1 += n
        b1 += n
    # Area below the x-axis
    a1 = 0
    b1 = n
    while b1 <= 1: # Root is 1
        # subtracts to "add" the negative value
        trapArea -= ((h_(a1) + h_(b1))/2)*(b1-a1)
        a1 += n
        b1 += n
    # Double the area for the other half of the heart
    return trapArea*2.0
heart = heartArea(math.pow(10, -5))
print("Area of the heart is " + str(heart))

#Calculate the area of the max circle enclosed by the heart
def bottomCircle(x, r):
    return -math.sqrt(math.pow(r,2)-math.pow(x,2)) - r + math.sqrt(2)

def intersectionTest(x1, x2, r, increments, epsilon):
    interectionctr = 0
    while x1 <= x2:
        x1 += increments
        if x1 > r:
            break
        if abs(bottomCircle(x1, r) - h_(x1)) <= epsilon:
            interectionctr += 1
    return interectionctr


def findmaxcircleRadius(minr, maxr, increments, epsilon):
    #Crude binary search
    while abs(maxr) - abs(minr) >= epsilon:
        r = (maxr + minr)/2
        if intersectionTest(0, maxr, r, increments, epsilon) == 1:
            return r
        if intersectionTest(0, maxr, r, increments, epsilon) < 1:
            minr = r+increments
        if intersectionTest(0, maxr, r, increments, epsilon) > 1:
            maxr = r-increments
        #print("MaxR = " + str(maxr) + " R = " + ", " + "MinR = " + str(minr))
    #Approcximation rounding errors
    return r
circleArea = math.pow(findmaxcircleRadius(0, math.sqrt(2), math.pow(10, -5), math.pow(10, -5)),2)*math.pi
print("Area of the circle is " + str(circleArea))
print("Area of the remaining heart is " + str(heart-circleArea))