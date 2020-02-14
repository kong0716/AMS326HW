# Darren Kong
# 110770716
# AMS326HW1
# Problem1.2

import math

def f(x):
    return math.pow(2.020, (-(math.pow(x, 3.0)))) - math.pow(x, 3.0)*math.cos(math.pow(x, 4.0)) - 1.984

def bisection_method(a, b, epsilon):
    if f(a)*f(b) >= 0:
        print("Failed\n")
        return
    while abs(b-a) > epsilon :
        x = (a+b)/2
        if f(x) == 0:
            return x
        if f(a)*f(x) >= 0:
            a = x
        if f(b)*f(x) >= 0:
            b = x
    return x

# Numbers below are eyeballed
print("Root 1 is " + str(bisection_method(-1, -.08, math.pow(10, -5))))
print("Root 2 is " + str(bisection_method(1, 1.3, math.pow(10, -5))))
print("Root 3 is " + str(bisection_method(1.35, 1.5, math.pow(10, -5))))
print("Root 4 is " + str(bisection_method(1.6, 1.7, math.pow(10, -5))))
print("Root 5 is " + str(bisection_method(1.75, 1.9, math.pow(10, -5))))
print("Root 6 is " + str(bisection_method(1.9, 2, math.pow(10, -5))))