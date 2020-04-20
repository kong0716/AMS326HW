# Darren Kong
# 110770716
# AMS326
import matplotlib.pyplot as plt
import math

v_0 = 14
v_B1 = 7
v_B2 = 14
v_B3 = 21
a = 7777

#Runge Kutta Method
def w(x):
    return 4*v_0*((x/a) - ((x*x)/(a*a)))

def f(x, y, vb):
    return (y/x) - (w(x)/(vb*(x/math.sqrt((x*x) + (y*y)))))

def runge_kutta(f, x0, y0, h, vb):#Anything after h is other constants or variables not explicit in the original RK4
    k1 = f(x0, y0, vb)
    k2 = f(x0 + (.5*h), y0 + (.5*h*k1), vb)
    k3 = f(x0 + (.5*h), y0 + (.5*h*k2), vb)
    k4 = f(x0 + h, y0 + (h*k3), vb)
    tn1 = x0 + h
    yn1 = y0 + ((1/6)*h*(k1 + k2 + k3 + k4))
    return tn1 , yn1
xplot1 = list()
yplot1 = list()
xplot2 = list()
yplot2 = list()
xplot3 = list()
yplot3 = list()
x = 7777
y = 0
h = -.1
while x > 0:
    xplot1.append(x)
    yplot1.append(y)
    x, y = runge_kutta(f, x, y, h, v_B1)
x = 7777
y = 0
h = -.1
while x > 0:
    xplot2.append(x)
    yplot2.append(y)
    x, y = runge_kutta(f, x, y, h, v_B2)
x = 7777
y = 0
h = -.1
while x > 0:
    xplot3.append(x)
    yplot3.append(y)
    x, y = runge_kutta(f, x, y, h, v_B3)
plt.plot(xplot1, yplot1, 'r')
plt.plot(xplot2, yplot2, 'g')
plt.plot(xplot3, yplot3, 'b')
plt.xlabel("x")
plt.ylabel("y(x)")
plt.show()